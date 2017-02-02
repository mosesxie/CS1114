userNumber = int(input("Please enter a positive integer: "))

number = userNumber

thousands = number // 1000

remaining = number % 1000

fivehundreds = remaining // 500

remaining = remaining % 500

hundreds = remaining // 100

remaining = remaining % 100

fifties = remaining // 50

remaining = remaining % 50

tens = remaining // 10

remaining = remaining % 10

fives = remaining // 5

ones = remaining % 5

print("M" * thousands + "D" * fivehundreds + "C" * hundreds + "L" * fifties + "X" * tens + "V" * tens + "I" * ones)


    
    

    
