import math

n = int(input("Please enter an integer: "))

string = ""

for currentInt in range(1,n + 1):
    if math.pow(currentInt, 1/3).is_integer():
        string = string + "\n" +str(currentInt)
    
print(string)
