userCharacter = input("Enter a character: ")

if userCharacter.isupper():
    
    print(userCharacter + " is a upper case letter.")

elif userCharacter.islower():
    print(userCharacter + " is a lower case letter.")

elif userCharacter.isdigit():
    print(userCharacter + " is a digit.")

else:
    print(userCharacter + " is a non-alphanumeric character.")
