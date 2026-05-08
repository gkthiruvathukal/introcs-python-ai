def bmi_category(bmi: float) -> str:
    """Return the weight category for a given BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


if __name__ == '__main__':
    bmi = float(input("Enter BMI: "))
    print(bmi_category(bmi))
