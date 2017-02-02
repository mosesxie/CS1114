product = 1

a = 0

keepgoing = True

while keepgoing == True:
    integer = (input("Please enter a positive integer: "))

    if integer == "Done":
        keepgoing = False

    else:
        product = product * int(integer)
        a += 1

root = product ** (1/a)
rounded = round(root,4)

print("The geometric mean is:", rounded)
    

    
