kilogram = int(input("Please enter an integer for kilogram amount: "))

totalOunces = kilogram * 35.2736

totalPounds = totalOunces // 16

remainingOunces = totalOunces % 16

roundedOunces = round(remainingOunces, 5)

print(kilogram, "kilograms is", totalPounds, "pounds and ", roundedOunces, "ounces.")
