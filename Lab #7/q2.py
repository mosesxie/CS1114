from random import randint

number= randint(1,100)

a=int(input("Try to guess my number:"))

b=True

while b==True:
    if a>number:
        print("Wrong guess. My number is smaller than yours.")
    if a<number:
        print("Wrong guess. My number is bigger than yours.")
    a=int(input("Try to guess it:"))
    if a==number:
        print("Congrats! You guessed my number!")
        b=False
