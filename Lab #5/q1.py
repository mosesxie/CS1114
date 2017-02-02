n = int(input("Please enter an integer: "))
a = n
b = 1

string = ""

for currentNum in range(1, n+1):
    if(currentNum == 1):
        string = string + "\n " + ((" " * n)+"*")
    else:
        n-=1
        string = string + "\n " + ((" "*n) +"*"* (b + 2))
        b = b + 2

print(string) 
    
