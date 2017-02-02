n = int(input("Enter a positive integer: "))

for i in range (1, n+1):
    
    string = str(i)

    evenCounter = 0

    oddCounter = 0
    for currentChr in string:

        digit = int(currentChr)

        if digit % 2 == 0:
            evenCounter += 1

        else:
            oddCounter += 1


    if evenCounter > oddCounter:
        print(string)

        
        
