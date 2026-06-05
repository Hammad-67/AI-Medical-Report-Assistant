 🩺 AI Medical Report Explanation Agent

## Project Overview

AI Medical Report Explanation Agent is an intelligent healthcare assistance system that helps users understand medical laboratory reports using Artificial Intelligence and Large Language Models (LLMs).

Medical reports often contain complex terminology and numerical values that are difficult for non-medical users to understand. This project simplifies laboratory reports by generating patient-friendly explanations and allowing users to ask follow-up questions through a conversational interface.

The system supports both PDF and image-based medical reports and provides healthcare-related explanations using Google's Gemini AI model.


## Problem Statement

Patients frequently receive laboratory reports containing technical medical information that can be difficult to interpret without professional assistance.

Common challenges include:

* Understanding abnormal test results
* Interpreting medical terminology
* Identifying important findings
* Knowing when to seek professional medical advice

The proposed system addresses these challenges by providing simple and understandable explanations of medical reports.


## Objectives

The main objectives of this project are:

* Analyze medical laboratory reports using AI
* Support PDF and image-based reports
* Explain medical findings in simple language
* Detect abnormal report values
* Provide healthcare-related information
* Enable conversational interaction with users
* Improve healthcare literacy


## Key Features

### 📄 Medical Report Analysis

Users can upload:

* PDF laboratory reports
* JPG images
* JPEG images
* PNG images

The system extracts report information and generates explanations.

### 🤖 AI-Powered Explanations

The Gemini Large Language Model interprets report findings and provides simplified explanations for non-medical users.

### 💬 Conversational Healthcare Assistant

Users can ask healthcare-related questions such as:

* What does low hemoglobin mean?
* Explain my blood test results.
* What are the abnormalities in my report?
* What is diabetes?

### 🖼️ Image-Based Report Support

The system supports scanned reports and report images through OCR and AI-based document understanding.

### 📊 Report Summarization

Users can request:

* Report summaries
* Abnormality explanations
* Important observations
* Healthcare recommendations


## System Architecture

The system follows a layered architecture consisting of:

### 1. User Interface Layer

Developed using Streamlit.

Responsibilities:

* User interaction
* File upload
* Chat interface
* Result presentation

### 2. File Processing Layer

Handles:

* PDF reports
* Medical images
* File validation
* File management

### 3. OCR Layer

Responsible for:

* Text extraction
* Scanned document processing
* Image-based report support

### 4. AI Analysis Layer

Powered by Gemini AI.

Responsibilities:

* Medical report interpretation
* Healthcare question answering
* Abnormality detection
* Response generation

### 5. Response Layer

Responsible for:

* Formatting responses
* Displaying analysis
* Maintaining chat history


## Workflow

User Uploads Report
          ↓
File Processing
          ↓
OCR / Text Extraction
          ↓
Gemini AI Analysis
          ↓
Medical Explanation
          ↓
User Follow-up Questions
          ↓
AI Responses

## Technologies Used

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python     | Backend Development     |
| Streamlit  | User Interface          |
| Gemini API | Artificial Intelligence |
| OCR        | Text Extraction         |
| GitHub     | Version Control         |
| VS Code    | Development Environment |


## Installation Guide

### Step 1: Clone Repository

git clone https://github.com/Hammad-67/AI-Medical-Report-Assistant.git
cd AI-Medical-Report-Assistant

### Step 2: Create Virtual Environment

python -m venv venv

Activate environment:

**Windows**

venv\Scripts\activate

**Linux / Mac**

source venv/bin/activate

### Step 3: Install Dependencies

pip install -r requirements.txt

### Step 4: Configure Gemini API Key

Create a `.env` file in the project root directory.

GEMINI_API_KEY=YOUR_GEMINI_API_KEY


### Step 5: Run Application

streamlit run gui_app.py


The application will start at:

http://localhost:8501


## Project Structure

AI_Medical_Report_Agent/
│
├── gui_app.py
├── ai_engine.py
├── analyzer.py
├── formatter.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── home_page.png
│   ├── report_upload.png
│   ├── report_analysis.png
│   └── chatbot.png
│
└── docs/
    └── research_paper.pdf


## Usage Guide

### Analyze Medical Reports

1. Launch the application.
2. Upload a medical report (PDF/Image).
3. Wait for upload confirmation.
4. Ask:

Analyze my report

or

Summarize my report

The AI assistant will explain:

* Important findings
* Abnormal values
* Possible health implications
* Recommendations

---

### Ask General Health Questions

Examples:

What is diabetes?


What causes low hemoglobin?


Explain high cholesterol.


The AI assistant responds in simple and understandable language.


## Example Use Cases

### Use Case 1

Input:

Analyze my report


Output:

Your hemoglobin level is below the normal range, which may indicate anemia.


### Use Case 2

Input:

What does Vitamin D deficiency mean?

Output:


Vitamin D deficiency may affect bone health and immune system function.




## Screenshots
<img width="954" height="483" alt="image" src="https://github.com/user-attachments/assets/32a4f088-3c2b-462f-84c9-483864cee902" />
<img width="1910" height="1013" alt="image" src="https://github.com/user-attachments/assets/9c0ebf3f-810a-44a0-9d21-5a1323545764" />


Add screenshots of your project here.

### Home Page

Insert screenshot:



### Report Upload

Insert screenshot:


screenshots/report_upload.png


### Report Analysis

Insert screenshot:


screenshots/report_analysis.png


### Chat Interface

Insert screenshot:


screenshots/chatbot.png


## Future Enhancements

Planned improvements include:

* Voice-based healthcare assistant
* Multilingual support
* Mobile application
* Electronic Health Record (EHR) integration
* Improved OCR accuracy
* Medical trend analysis
* Personalized healthcare recommendations


## Limitations

* The system depends on external AI APIs.
* OCR accuracy may vary with image quality.
* AI responses should not be considered professional medical diagnosis.
* Users should consult healthcare professionals for medical decisions.


## Academic Information

This project was developed as part of the Artificial Intelligence course project for the Software Engineering program.

### Project Title

AI-Powered Medical Report Explanation Agent Using Large Language Models

### Domain

Artificial Intelligence in Healthcare

### Research Area

* Natural Language Processing
* Healthcare Informatics
* Large Language Models
* Conversational AI


## Author

**Hammad Amjad**

Software Engineering Department

University of Engineering and Technology Taxila

GitHub:

https://github.com/Hammad-67



This project is developed for educational and research purposes only.


