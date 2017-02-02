#inputs string and outputs middle character, first half, and second half

userString = input("Enter a string of odd length: ") #take user input

middleIndex = len(userString) // 2 #finds the middle index

middleCharacter = userString[middleIndex] # finds the middle character

print("Middle Character:", middleCharacter)

print("First half: " + userString[:middleIndex])

print("Second half: " + userString[middleIndex+1:])
