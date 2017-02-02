userString = input("Please enter a string: ")


adjustedString = ""

for currentChr in userString:

    if currentChr.isupper():

        adjustedString = adjustedString + currentChr.lower()


    else:

        adjustedString = adjustedString + currentChr.upper()


print(adjustedString)
