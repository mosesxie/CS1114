n = int(input("Enter a positive integer: "))

string = ""

for i in range(1, n+1):
    k = n-i
    string =' ' + string

    for b in range (1, i +1):
        a = str(b)
        string =  string + a

    string = string + "\n" + ' '* k 

print(string)

        
