userString = input("Please enter a line of text: ")

userCharacter = input("Please enter the character you want to remove: ")

newString = ""

for currentChr in userString:

    if userCharacter != currentChr:
        newString = newString + currentChr


print(newString)
        
