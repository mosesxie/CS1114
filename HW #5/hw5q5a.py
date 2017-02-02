sequenceLength = int(input("Please enter the length of the sequence: "))

product = 1

for i in range(0,sequenceLength):
    integer = int(input("Please enter a positive integer: "))

    product = product * integer


root = product ** (1/sequenceLength)
rounded = round(root, 4)

print("The geometric mean is:", rounded)

    
