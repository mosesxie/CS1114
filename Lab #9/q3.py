def sum_of_squares(lst):

    squaresSum = 0

    for index in lst:

        squaresSum = squaresSum + int(index)**2


    return squaresSum

def main():

    userInput = "0"

    userList = []

    while userInput != "done":

        userInput = input("Enter a number for the list: ")

        if userInput != "done":

            userList.append(userInput)


    final = sum_of_squares(userList)

    print(final)

main()

        
