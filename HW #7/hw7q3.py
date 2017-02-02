# Moses Xie
# mx407
# hw7q3
# Make a counter for the 5 tries and a boolean for the correctness
# breaks it after one of them changes 

from random import randint


print("I thought of a number between 1 and 100! Try to guess it.")


number = randint(1,100)

counter = 1

flag = False

top = 100
bottom = 1

while counter <= 5 and flag == False:
    userAnswer = int(input("Try to guess what it is: "))

    if userAnswer == number:
        flag = True

    elif userAnswer > number:
        top = userAnswer - 1
        print("Wrong guess! Guess in range", top, "to", bottom, "You have",\
              5 - counter, "tries left.")
        
    else:
        bottom = userAnswer + 1
        print("Wrong guess! Guess in range", bottom, "to", top, "You have"\
              ,5 - counter, "tries left.")

    counter += 1

if flag == True:
    print("Good Job, You won in" , counter - 1, "tries")

else:
    print("Sorry, You lost")
        
