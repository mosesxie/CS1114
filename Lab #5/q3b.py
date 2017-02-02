userString = input("Please enter a string: ")

userLetter = input("Please enter a letter: ")

counter = 0

num = 0

while counter != len(userString):
    if userString[counter] == userLetter:
        num += 1

    counter+=1

print("Letter " + userLetter + " appears", num, "times in the string." )
    
    
    
