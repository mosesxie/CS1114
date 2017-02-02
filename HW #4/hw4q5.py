userPassword = input("Enter a password:")

digitCounter = 0

upperCounter = 0

lowerCounter = 0

specialCounter = 0

for currentCharacter in userPassword:
    if currentCharacter.isdigit():
        digitCounter += 1

    elif currentCharacter.isupper():
        upperCounter += 1

    elif currentCharacter.islower():
        lowerCounter += 1

    else:
        specialCounter += 1

if digitCounter >= 2 and upperCounter >= 2 and lowerCounter >= 2 and specialCounter >= 1:
    print(userPassword + " is a valid password.")

else:
    print(userPassword + " is an invalid password. ")
