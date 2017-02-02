userString = input("Please enter an integer: ")

even = 0

odd = 0

for currentChar in userString:
    currentInt = int(currentChar)
    if currentInt % 2 == 0:
        even +=1

    else:
        odd +=1

print("Even =", even)
print("Odd =", odd)
