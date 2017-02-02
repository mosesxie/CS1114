# Moses Xie
# mx407
# hw7q1
#
# encrypts every charcter by going over every char detecting if its
# a lowercase, uppercase, or special character then encrypting it accordingly


userShift = int(input("Shift by: "))

userString = input("Enter a string with at lest one capital letter: ")

encryptedString = ""

for currentChr in userString:

    if currentChr.islower():

        trueUnicode = ord(currentChr)

        shiftedUnicode = trueUnicode - ord("a")

        encryptedshiftedUnicode = (shiftedUnicode + userShift) % 26

        encryptedUnicode = encryptedshiftedUnicode + ord("a")

        encryptedCharacter = chr(encryptedUnicode)

        encryptedString = encryptedString + encryptedCharacter

        

    elif currentChr.isupper():

        trueUnicode = ord(currentChr)

        shiftedUnicode = trueUnicode - ord("A")

        encryptedshiftedUnicode = (shiftedUnicode + userShift) % 26

        encryptedUnicode = encryptedshiftedUnicode + ord("A")

        encryptedCharacter = chr(encryptedUnicode)

        encryptedString = encryptedString + encryptedCharacter

    else:
        encryptedString = encryptedString + currentChr

print(encryptedString)        
