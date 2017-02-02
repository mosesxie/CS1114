userInteger = int(input("Please enter an integer: "))

factorial = 1

for multiplier in range(1,userInteger + 1):
    factorial = factorial * multiplier

print(factorial)
