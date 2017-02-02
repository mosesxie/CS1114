userWeight = float(input("Please enter weight in kilograms: "))

userHeight = float(input("Please enter height in meters: "))

BMI = (userWeight)/(userHeight**2)

if (BMI < 18.5):
    print("Underweight")

elif (BMI >= 18.5 and BMI <=24.9 ):
    print("Normal")

elif (BMI >= 25 and BMI <= 29.9):
    print("Overweight")

else:
    print("Obese")

print("BMI is:", BMI)
