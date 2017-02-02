import math

firstLength = int(input("Please enter the first length: "))

secondLength = int(input("Please enter the second length: "))

thirdLength = int(input("Please enter the third length: "))

if(firstLength > secondLength and firstLength > thirdLength):
    greatestLength = firstLength
    if (secondLength > thirdLength):
        middleLength = secondlength
        smallestLength = thirdlength
    else:
        middleLength = thirdLength
        smallestLength = secondLength

elif(secondLength > firstLength and secondLength > thirdLength):
    greatestLength = secondLength
    if (firstLength > thirdLength):
        middleLength = firstlength
        smallestLength = thirdlength
    else:
        middleLength = thirdLength
        smallestLength = firstLength

else:
    greatestLength = thirdLength
    if (secondLength > firstLength):
        middleLength = secondLength
        smallestLength = firstLength
    else:
        middleLength = firstLength
        smallestLength = secondLength

if(greatestLength**2 == middleLength**2 + smallestLength**2):
    print(firstLength, ",", secondLength, ",", thirdLength, "forms a right triangle")

else:
    print("It does not form a right triangle.")
    
    
