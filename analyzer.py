# Medical reference ranges

reference_ranges = {

    "Hemoglobin": (13, 17),
    "WBC": (4000, 11000),
    "Platelets": (150000, 450000),
    "RBC": (4.5, 5.9),
    "Glucose": (70, 140),
    "Creatinine": (0.7, 1.3),
    "Urea": (7, 20),
    "Sodium": (136, 145),
    "Potassium": (3.5, 5.1),
    "TSH": (0.4, 4.0),
    "Cholesterol": (125, 200),
    "Vitamin D": (20, 50)

}


parameter_aliases = {

    "Platelet Count": "Platelets",
    "Platelet": "Platelets",
    "White Blood Cells": "WBC",
    "White Blood Cell": "WBC",
    "Red Blood Cells": "RBC",
    "Blood Sugar": "Glucose",
    "Fasting Blood Sugar": "Glucose",
    "Vitamin B12": "Vitamin D",
    "Sodium (Na+)": "Sodium",
    "Potassium (K+)": "Potassium",
    "25(OH) Vitamin D": "Vitamin D",
    "25 OH Vitamin D": "Vitamin D",
    "Vitamin D3": "Vitamin D"
}


def analyze_parameter(parameter, value):

    if parameter in parameter_aliases:
        parameter = parameter_aliases[parameter]

    if parameter not in reference_ranges:
        return "UNKNOWN"

    low, high = reference_ranges[parameter]

    # Critical conditions
    if value < (low * 0.5):
        return "CRITICAL LOW"

    elif value > (high * 1.5):
        return "CRITICAL HIGH"

    # Normal abnormal conditions
    elif value < low:
        return "LOW"

    elif value > high:
        return "HIGH"

    else:
        return "NORMAL"


def get_normal_range(parameter):

    if parameter in parameter_aliases:
        parameter = parameter_aliases[parameter]

    if parameter in reference_ranges:
        low, high = reference_ranges[parameter]
        return f"{low} - {high}"

    return "Unknown"