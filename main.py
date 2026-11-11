
# BMI Calculator
# Oasis Infobyte Internship - Python Programming

print("====================================")
print("          BMI CALCULATOR")
print("====================================")

try:
    # Taking input from the user
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in metres: "))

    # Checking whether the input is valid
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be greater than zero.")

    else:
        # Calculating BMI
        bmi = weight / (height ** 2)

        # Finding BMI category
        if bmi < 18.5:
            category = "Underweight"

        elif bmi < 25:
            category = "Normal Weight"

        elif bmi < 30:
            category = "Overweight"

        else:
            category = "Obese"

        # Displaying the result
        print("\n========== BMI RESULT ==========")
        print("Your BMI is:", round(bmi, 2))
        print("Your BMI Category is:", category)
        print("================================")

except ValueError:
    print("Invalid input! Please enter numbers only.")

print("\nThank you for using BMI Calculator!")


