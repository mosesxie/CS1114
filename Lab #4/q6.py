userPassword = input("Please enter a password: ")
counter = 0

while counter < len(userPassword):
    if userPassword[counter].isupper():
        counter = 100
    else: counter = counter + 1



if(len(userPassword) >= 6 and counter == 100):
    print("This password is valid")

else:
    print("This password is invalid")
