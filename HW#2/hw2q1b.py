userWeight = float(input("Please enter weight in pounds: "))

userHeight = float(input("Please enter height in inches: "))

metricWeight = userWeight * 0.453592

metricHeight = userHeight * 0.0254

BMI = (metricWeight)/(metricHeight**2)

print("BMI is:", BMI)
