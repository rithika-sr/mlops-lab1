from src.bmi import bmi, category

def main():
    # Ask user for weight and height
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    # Calculate BMI
    bmi_value = bmi(weight, height)
    print(f"BMI: {bmi_value}")

    # Get category
    print(f"Category: {category(bmi_value)}")

if __name__ == "__main__":
    main()
