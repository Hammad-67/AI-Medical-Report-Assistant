import streamlit as st
from ai_engine import (
    generate_ai_summary,
    analyze_medical_image,
    analyze_medical_pdf,
    medical_chatbot
)


# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_report" not in st.session_state:
    st.session_state.uploaded_report = ""

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None


# Page config
st.set_page_config(
    page_title="AI Medical Report Assistant",
    page_icon="🩺",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    color: #4CAF50;
    text-align: center;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background-color: #4CAF50;
    color: white;
    font-size: 18px;
}

.stTextArea textarea {
    font-size: 16px;
}

/* =========================
   CLEAN FILE UPLOADER
========================= */

[data-testid="stFileUploader"] {
    width: 45px;
}

/* Remove drag/drop area */
[data-testid="stFileUploaderDropzone"] {
    border: none;
    background: transparent;
    padding: 0;
    min-height: 0;
}

/* Remove extra container styling */
[data-testid="stFileUploader"] section {
    border: none;
    padding: 0;
    background: transparent;
}

/* Hide text only */
[data-testid="stFileUploader"] small {
    display: none;
}

/* Hide "Drag and drop" text */
[data-testid="stFileUploader"] p {
    display: none;
}

/* Keep button visible and styled */
[data-testid="stBaseButton-secondary"] {

    height: 45px !important;
    width: 45px !important;

    min-width: 45px !important;

    border-radius: 12px !important;

    background-color: #1E1E1E !important;

    border: 1px solid #333 !important;

    display: flex !important;

    align-items: center !important;

    justify-content: center !important;

    font-size: 18px !important;

    padding: 0 !important;
}

</style>
""", unsafe_allow_html=True)

# Main title
st.title("🩺 AI Medical Report Explanation Agent")

st.caption(
    "AI-powered healthcare assistant for interpreting laboratory reports"
)

# Sidebar
with st.sidebar:

    st.header("About")

    st.write(
        """
        This AI-powered system analyzes laboratory reports and provides:

        - Medical parameter analysis
        - Abnormality detection
        - Simple explanations
        - Health recommendations
        """
    )

    st.divider()

    if st.sidebar.button("🗑️ New Chat"):

        st.session_state.messages = []

        st.session_state.uploaded_report = ""

        st.session_state.uploaded_file = None

        st.rerun()

    st.write("Developed as AI Course Project")

# ==============================
# DISPLAY CHAT HISTORY
# ==============================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ==============================
# CLEAN CHAT TOOLBAR
# ==============================

st.markdown("---")

toolbar_col1, toolbar_col2 = st.columns([0.7, 12])

with toolbar_col1:

    uploaded_file = st.file_uploader(
        "📎",
        type=["pdf", "jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

with toolbar_col2:

    user_prompt = st.chat_input(
        "Ask health questions or talk about uploaded medical reports..."
    )


# ==============================
# HANDLE FILE UPLOAD
# ==============================

if uploaded_file is not None:

    st.session_state.uploaded_file = uploaded_file

    if "report_uploaded" not in st.session_state:

        st.session_state.messages.append({
            "role": "assistant",
            "content":
            "📄 Report uploaded successfully. Ask me to analyze it."
        })

        st.session_state.report_uploaded = True

        st.rerun()


# ==============================
# HANDLE USER CHAT
# ==============================

if user_prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    # Show user message
    with st.chat_message("user"):

        st.markdown(user_prompt)

    report_keywords = [
        "report",
        "lab report",
        "medical report",
        "analyze",
        "analyse",
        "summarize",
        "summary",
        "explain",
        "abnormal",
        "abnormalities",
        "blood test",
        "cbc",
        "attached report",
        "uploaded report"
    ]

    question = user_prompt.lower()

    # AI response
    with st.chat_message("assistant"):

        with st.spinner("AI is thinking..."):

            if any(keyword in question for keyword in report_keywords):

                if st.session_state.uploaded_file is not None:

                    file_type = st.session_state.uploaded_file.type

                    if "image" in file_type:

                        ai_response = analyze_medical_image(
                            st.session_state.uploaded_file
                        )

                    elif "pdf" in file_type:

                        ai_response = analyze_medical_pdf(
                            st.session_state.uploaded_file
                        )

                else:

                    ai_response = (
                        "Please upload a medical report first."
                    )

            else:

                ai_response = medical_chatbot(
                    user_prompt,
                    st.session_state.uploaded_report
                )

            st.markdown(ai_response)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    st.rerun()