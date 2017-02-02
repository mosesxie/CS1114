userName = input("Please enter your name: ")

graduationYear = int(input("Please enter your graduation year: "))

currentYear = int(input("Please enter current year: "))

difference = graduationYear - currentYear

if (currentYear > graduationYear):
    print(userName, "has graduated")

elif (difference > 4):
    print(userName, "is not in college yet")

elif(difference == 4):
    print(userName, "is a Freshman")

elif(difference == 3):
    print(userName, "is a Sophmore")

elif(difference == 2):
    print(userName, "is a Junior")

elif(difference == 1):
    print(userName, "is a Senior")

