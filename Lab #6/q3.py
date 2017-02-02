string1 = input("Please enter name 1: ")

string2 = input("Please enter name 2: ")

commaIndex = string1.find(",")

spaceIndex = string2.find(" ")

if string1[:commaIndex] == string2[spaceIndex + 1:] and string1[commaIndex+2:] == string2[:spaceIndex]:
    print("The two names are equal! ")

else:
    print("The two names are not the same. ")
