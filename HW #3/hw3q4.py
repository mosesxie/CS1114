import math

print("Please enter lengths of a triangle's sides")

firstLength = float(input("Length of the first side: "))

secondLength = float(input("Length of the second side: "))

thirdLength = float(input("Length of the third side: "))

if (firstLength > secondLength and firstLength > thirdLength):
    largestSide = firstLength
    leg = secondLength

elif(secondLength > firstLength and secondLength > thirdLength):
    largestSide = secondLength
    leg = thirdLength
else:
    largestSide = thirdLength
    leg = firstLength

if (firstLength == secondLength == thirdLength):
    print("This is an equilateral triangle")

elif(firstLength != secondLength != thirdLength):
    print("This triangle is neither an equilateral nor a isoceles triangle")

elif(largestSide == leg * math.sqrt(2)):
    print("This is an isosceles right triangle")

else:
    print("This is an isoceles triangle")
