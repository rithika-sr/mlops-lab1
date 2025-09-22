def bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    return round(weight / (height ** 2), 2)

def category(bmi_value):
    """Return BMI category."""
    if bmi_value < 18.5:
        return "Underweight"
    elif 18.5 <= bmi_value < 24.9:
        return "Normal"
    elif 25 <= bmi_value < 29.9:
        return "Overweight"
    else:
        return "Obese"
