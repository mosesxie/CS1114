userString = input("Enter a word: ")

vowelCounter = 0

consonantCounter = 0

for currentCharacter in userString:
    if currentCharacter == "a" or currentCharacter == "e" or currentCharacter == "i" or currentCharacter == "o" or currentCharacter == "u":
        vowelCounter += 1
    else:
        consonantCounter += 1

print(userString + " has", vowelCounter, "vowels and", consonantCounter, "consonants.")
        
