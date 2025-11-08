print("Welcome to the BMI Calculator!\n")

name = input("Enter your name: ")
height = float(input("Enter your height in meters (e.g. 1.75): "))
weight = float(input("Enter your weight in kilograms (e.g. 68): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight 😕"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight 😊"
elif 25 <= bmi < 29.9:
    category = "Overweight 😐"
else:
    category = "Obese 😟"

print("\n==============================")
print(f"Hello, {name}!")
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")
print("==============================")

if bmi < 18.5:
    print("Tip: Try to include more healthy calories and proteins in your diet.")
elif bmi > 24.9:
    print("Tip: Regular exercise and balanced meals can help maintain a healthy weight.")
else:
    print("Great job! Keep up your healthy habits!")
