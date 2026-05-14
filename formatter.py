def generate_explanation(parameter, status):

    explanations = {

        "Hemoglobin": {
            "LOW": "Hemoglobin is below normal. This may indicate anemia or reduced oxygen-carrying capacity.",
            "HIGH": "Hemoglobin is above normal. This may occur due to dehydration or other conditions.",
            "NORMAL": "Hemoglobin level is within the normal range."
        },

        "WBC": {
            "LOW": "Low WBC count may weaken the body's ability to fight infections.",
            "HIGH": "High WBC count may indicate infection or inflammation.",
            "NORMAL": "WBC count is within the normal range."
        },

        "Platelets": {
            "LOW": "Low platelet count may affect blood clotting and increase bleeding risk.",
            "HIGH": "High platelet count may increase clotting risk.",
            "NORMAL": "Platelet count is within the normal range."
        },

        "RBC": {
            "LOW": "Low RBC count may indicate anemia or blood loss.",
            "HIGH": "High RBC count may occur due to dehydration or lung conditions.",
            "NORMAL": "RBC count is within the normal range."
        },

        "Glucose": {
            "LOW": "Low glucose may cause dizziness, weakness, or fainting.",
            "HIGH": "High glucose may indicate diabetes or poor blood sugar control.",
            "NORMAL": "Blood glucose level is normal."
        },

        "Creatinine": {
            "LOW": "Low creatinine is usually not serious but may relate to low muscle mass.",
            "HIGH": "High creatinine may indicate kidney function problems.",
            "NORMAL": "Creatinine level is within the normal range."
        },

        "Urea": {
            "LOW": "Low urea levels are generally not serious.",
            "HIGH": "High urea may indicate dehydration or kidney-related issues.",
            "NORMAL": "Urea level is within the normal range."
        },

        "TSH": {
            "LOW": "Low TSH may suggest hyperthyroidism.",
            "HIGH": "High TSH may suggest hypothyroidism.",
            "NORMAL": "TSH level is within the normal range."
        },

        "Cholesterol": {
            "LOW": "Low cholesterol is generally not harmful.",
            "HIGH": "High cholesterol may increase heart disease risk.",
            "NORMAL": "Cholesterol level is within the normal range."
        },

        "Vitamin D": {
            "LOW": "Low Vitamin D may affect bone health and immunity.",
            "HIGH": "High Vitamin D may occur due to excessive supplementation.",
            "NORMAL": "Vitamin D level is within the normal range."
        },

        "Sodium": {
            "LOW": "Low sodium may cause weakness, confusion, or dehydration.",
            "HIGH": "High sodium may indicate dehydration or kidney-related issues.",
            "NORMAL": "Sodium level is within normal range."
        },

        "Potassium": {
            "LOW": "Low potassium may affect muscle and heart function.",
            "HIGH": "High potassium may affect heart rhythm and requires attention.",
            "NORMAL": "Potassium level is within normal range."
        }
    }

    if parameter in explanations:

        if status in explanations[parameter]:
            return explanations[parameter][status]

    return "No explanation available."


def generate_summary(status_list):

    summary = []

    if "CRITICAL LOW" in status_list or "CRITICAL HIGH" in status_list:
        summary.append(
            "Some parameters are critically abnormal and may require urgent medical attention."
        )

    if "LOW" in status_list:
        summary.append("Some parameters are below normal range.")

    if "HIGH" in status_list:
        summary.append("Some parameters are above normal range.")

    if all(status == "NORMAL" for status in status_list):
        summary.append("All parameters are within normal range.")

    recommendation = (
        "Please consult a healthcare professional for proper medical advice."
    )

    return " ".join(summary), recommendation