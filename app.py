import requests
from formatter import generate_explanation, generate_summary
from analyzer import analyze_parameter
from dotenv import load_dotenv
import os
import re
from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

API_KEY = os.getenv("HF_API_KEY")

print("====================================")
print(" AI Medical Report Explanation Agent ")
print("====================================")

print("\nPaste Medical Report:")
print("Type END on a new line when finished.\n")

# Multi-line input
lines = []

while True:
    line = input()

    if line.upper() == "END":
        break

    lines.append(line)

# Combine report
user_report = "\n".join(lines)
print("\n========== PARAMETER ANALYSIS ==========\n")

report_lines = user_report.split("\n")
all_status = []

for item in report_lines:

    try:
        parameter, rest = item.split(":")
        parameter = parameter.strip()

        number = re.findall(r"\d+\.?\d*", rest)[0]
        value = float(number)

        status = analyze_parameter(parameter, value)
        all_status.append(status)

        explanation = generate_explanation(parameter, status)

        print(f"\n{parameter}")
        print(f"Value: {value}")
        print(f"Status: {status}")
        print(f"Explanation: {explanation}\n")

    except:
        print(f"Could not analyze: {item}")
        print("\n========== OVERALL SUMMARY ==========\n")

        

summary, recommendation = generate_summary(all_status)

print(summary)

print("\nRecommendation:")
print(recommendation)

# Final prompt
final_prompt = f"""
{SYSTEM_PROMPT}

Medical Report:
{user_report}
"""

# Hugging Face API URL
# API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# payload = {
#     "inputs": final_prompt
# }

# # Send request

# response = requests.post(
#     API_URL,
#     headers={
#         "Authorization": f"Bearer {API_KEY}"
#     },
#     json={
#         "inputs": final_prompt
#     }
# )

# print("\n========== AI RESPONSE ==========\n")

# print("Status Code:", response.status_code)

# try:
#     result = response.json()
#     print(result)
# except Exception:
#     print(response.text)