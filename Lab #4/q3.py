oldNumber = input("Enter your phone number in the form XXX-XXX-XXXX: ")


newNumber = "646-997"

if oldNumber[:7] == "718-260":
    newNumber = newNumber + oldNumber[7:]
    print("Your new number is " + newNumber)

else:
    print("This is not a valid NYU SOE phone number")
    
