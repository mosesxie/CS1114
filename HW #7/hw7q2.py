# Moses Xie
# mx407
# hw7q2
#
# first for loop for the horizontal second for the vertical
# using the iterators to find the values and add them to a string


string = ""

number = 0

stringNumber = ""

for column in range(1,6):

    for row in range (1,11):

        number = row ** column

        stringNumber = str(number)

        string = string + "\t" + stringNumber
        

    string = string + "\n"

print(string)
        
        
