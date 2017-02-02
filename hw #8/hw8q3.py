# Moses Xie
# mx407
# hw8q3
#
# Used previous code for one function
# other function is a loop of the other function to create different sections of the tree

def triangle(n, char, m):

    number_of_asterisks = 1
    number_of_spaces = n-1 + m
    for i in range(1, n+1):
        line = ' '*number_of_spaces + char*number_of_asterisks
        print(line)
        number_of_asterisks = number_of_asterisks+2
        number_of_spaces = number_of_spaces-1


def maketree(p, char, m):

    m = m + p

    for i in range(1,p+1):

        triangle(i + 1, char, m)

        m -= 1

def main():

    userP = int(input("Enter N: "))

    userChar = input("Enter Character: ")

    userM = int(input("Enter M: "))

    maketree(userP,userChar,userM)
    



main()
