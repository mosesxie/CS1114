userCharacter = input("Enter a character: ")

if ord(userCharacter) <= 122 and ord(userCharacter) >= 97:
    print(userCharacter + " is a lower case letter")

elif ord(userCharacter) >= 65 and ord(userCharacter) <= 90:
    print(userCharacter + " is an upper case letter")

elif ord(userCharacter) <= 57 and ord(userCharacter) >= 48:
    print(userCharacter + " is a digit")

else:
    print(userCharacter + " is a special character")
