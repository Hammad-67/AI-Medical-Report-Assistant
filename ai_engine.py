import google.generativeai as genai
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load Gemini model
model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)


def generate_ai_summary(report_text):

    prompt = f"""
    You are an AI medical assistant.

    Analyze the following medical laboratory report.

    Explain abnormal findings in simple language.

    Mention possible health concerns briefly.

    Keep response short and understandable for non-medical users.

    Medical Report:
    {report_text}
    """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"AI Error: {str(e)}"


def medical_chatbot(user_question, report_text):

    prompt = f"""
    You are an AI healthcare assistant.

    The user already uploaded this medical report:

    {report_text}

    User Question:
    {user_question}

    Answer in simple language.

    Do not provide final medical diagnosis.

    Encourage consulting a doctor for serious concerns.
    """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"AI Error: {str(e)}"