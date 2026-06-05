import google.generativeai as genai
import streamlit as st
import os
from PIL import Image
import tempfile

from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ==========================
# API KEY HANDLING
# ==========================

try:
    # Streamlit Cloud
    API_KEY = st.secrets["GEMINI_API_KEY"]

except Exception:
    # Local Development
    API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
print("Loaded API Key:", API_KEY[:15])
genai.configure(api_key=API_KEY)

# Load Model
model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)


def analyze_medical_image(uploaded_file):

    prompt = """
    You are an AI Medical Report Assistant.

    Analyze this medical report image.

    Extract important medical parameters.

    Explain:
    - Abnormal findings
    - Normal findings
    - Possible health implications

    Use simple language.

    Do not provide a final diagnosis.

    Recommend consulting a doctor if necessary.
    """

    try:

        image = Image.open(uploaded_file)

        response = model.generate_content(
            [prompt, image]
        )

        return response.text

    except Exception as e:
        error = str(e)

        if "429" in error:

            return """
            Gemini quota exceeded.

            Please wait a few minutes and try again.
            """

        return f"AI Error: {error}"


# pdf function upload

def analyze_medical_pdf(uploaded_file):

    try:

        prompt = """
        You are an AI Medical Report Assistant.

        Analyze this medical report PDF.

        Extract:
        - Medical parameters
        - Test values
        - Abnormal findings
        - Possible health implications

        Explain everything in simple language.

        Do not provide a final diagnosis.
        """

        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(uploaded_file.read())

            temp_path = tmp.name

        pdf_file = genai.upload_file(temp_path)

        response = model.generate_content(
            [prompt, pdf_file]
        )

        return response.text

    except Exception as e:
        error = str(e)

        if "429" in error:

            return """
            Gemini quota exceeded.

            Please wait a few minutes and try again.
            """

        return f"AI Error: {error}"


# ==========================
# REPORT ANALYSIS
# ==========================

def generate_ai_summary(report_text):

    prompt = f"""
    You are an AI Medical Report Explanation Assistant.

    Analyze the uploaded laboratory report.

    Explain:
    - Abnormal findings
    - Possible health implications
    - Important observations
    - Recommendations

    Use simple language understandable by non-medical users.

    Do NOT provide a final diagnosis.

    Medical Report:

    {report_text}
    """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        error = str(e)

        if "429" in error:

            return """
            Gemini quota exceeded.

            Please wait a few minutes and try again.
            """

        return f"AI Error: {error}"


# ==========================
# HEALTH CHATBOT
# ==========================

def medical_chatbot(user_question, report_text=""):

    prompt = f"""
    You are an AI Healthcare Assistant.

    Uploaded Medical Report:

    {report_text}

    User Question:

    {user_question}

    Rules:
    - Answer in simple language.
    - Explain medical concepts clearly.
    - If report data exists, use it.
    - Do not provide final diagnosis.
    - Recommend consulting a doctor for serious concerns.
    """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        error = str(e)

        if "429" in error:

            return """
            Gemini quota exceeded.

            Please wait a few minutes and try again.
            """

        return f"AI Error: {error}"