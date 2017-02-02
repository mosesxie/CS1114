userInteger = int(input("Please enter an an integer less than 100: "))

fifties = userInteger // 50

remainingAmount = userInteger % 50

tens = remainingAmount // 10

remainingAmount = remainingAmount % 10

fives = remainingAmount // 5

remainingAmount = remainingAmount % 5

singles = remainingAmount

romanNumeral = ""

if (fifties == 1):
    romanNumeral = "L"

if(tens == 4):
    romanNumeral = romanNumeral + "XXXX"
elif (tens == 3):
    romanNumeral = romanNumeral + "XXX"
elif(tens == 2):
    romanNumeral = romanNumeral + "XX"
elif(tens == 1):
    romanNumeral = romanNumeral + "X"

if (fives == 1):
    romanNumeral = romanNumeral + "V"

if(singles == 4):
    romanNumeral = romanNumeral + "IIII"
elif(singles ==3):
    romanNumeral = romanNumeral + "III"
elif(singles == 2):
    romanNumeral = romanNumeral + "II"
elif(singles == 1):
    romanNumeral = romanNumeral + "I"

print(romanNumeral)
