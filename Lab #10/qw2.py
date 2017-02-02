import random

def randomgen():
    lst=['rock','paper','scissors']
    index = random.randint(0,2)
    computer = lst[index]
    return computer

def winner(user, computer):

    if user == "paper" and computer == "rock":

        return "user"

    elif user == "rock" and computer == "scissors":

        return "user"

    elif user == "scissors" and computer == "paper":

        return "user"

    elif computer == "paper" and user == "rock":

        return "computer"

    elif computer == "rock" and user == "scissors":

        return "computer"

    elif computer == "scissors" and user == "paper":

        return "computer"

    elif user == computer:
        return "tie"


def main():

    userInput = ""

    while userInput != "Done":

        userInput = input("Enter your choice: ")

        computerChoice = randomgen()

        gameWinner = winner(userInput, computerChoice)

        print("The winner is ", gameWinner)

main()

    
        




    
    

    

    

    
