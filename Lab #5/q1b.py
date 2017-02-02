n = int(input("Please enter an integer: "))

string = ""

for currentChr in range(1,n+1):
    string = string + "\n" + "#" * (currentChr - 1) + "%" + ((n - currentChr) * "$")

print(string)
