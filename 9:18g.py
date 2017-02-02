firstFeet = int(input("Please enter the first length's feet:"))

firstInches = int(input("Please enter the first length's inches: "))

secondFeet = int(input("Please enter the second length's feet:"))

secondInches = int(input("Please enter the second length's inches: "))

firstTotal = (firstFeet * 12) + firstInches

secondTotal = (secondFeet * 12) + secondInches

totalInches = firstTotal + secondTotal

sumFeet = totalInches // 12

sumInches = totalInches % 12

print("Their sum is:", sumFeet, "feet and", sumInches, "inches.")
