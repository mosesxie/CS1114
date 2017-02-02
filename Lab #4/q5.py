

phrase = input("Please enter a three word phrase: ")

word = input("Please enter a word: ")

letters = input("Please enter a 3 letter word: ")

lettersPhrase = phrase[0]

space = phrase.find(" ")

lettersPhrase = lettersPhrase + " " + phrase[space+1]

space2 = phrase.find(" ", space + 1)

lettersPhrase = lettersPhrase + " " + phrase[space2 + 1]

print(lettersPhrase)

capitalWord = word.upper()

print(capitalWord)

s = ord(letters[0])

d = ord(letters[1])

a = ord(letters[2])

print(s, d, a)


