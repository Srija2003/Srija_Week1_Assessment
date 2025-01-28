def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_input_from_user():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    return weight, height

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight, height = get_input_from_user()
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")


main()
