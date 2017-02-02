initialInt = int(input("Please enter a three digit positive integer: "))

firstDigit = initialInt // 100

remainingInt = initialInt % 100

secondDigit = remainingInt // 10

remainingInt = initialInt % 10

thirdDigit = remainingInt

finalSum = firstDigit + secondDigit + thirdDigit

print("The sum of its digits is", finalSum)
