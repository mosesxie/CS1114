userString = input("Please enter a string: ")

userLetter = input("Please enter a letter: ")

count = 0

for currentChr in userString:
    if currentChr == userLetter:
        count += 1

print("Letter " + userLetter + " appears", count, "times in the string." )
