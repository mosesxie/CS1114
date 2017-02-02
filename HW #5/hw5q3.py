userString = input("Please enter a string of lowercase letters: ")

a = 0

chr1 = ""
chr2 = ""

lexigraphical = True

for currentIndex in range(0, len(userString)):
    chr1 = userString[a]
    chr2 = userString[a+1]

    if ord(chr1)>ord(chr2):
        lexigraphical = False


if lexigraphical == True:
    print(userString + " is increasing")

else:
    print(userString + " is not increasing")
    
    
