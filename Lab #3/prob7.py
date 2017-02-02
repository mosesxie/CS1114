month = int(input("PLease enter an integer between 1 and 12: "))

days = 0

if(month == 1):
    month1 = "January"
    days = 31

elif(month == 2):
    month1 = "February"
    days = 28

elif(month == 3):
    month1 = "March"
    days = 31
    
elif(month == 4):
    month1 = "April"
    days = 30
    
elif(month == 5):
    month1 = "May"
    days = 31
elif(month == 6):
    month1 = "June"
    days = 30
    
elif(month == 7):
    month1 = "July"
    days = 31
    
elif(month == 8):
    month1 = "August"
    days = 31
    
elif(month == 9):
    month1 = "September"
    days = 30
    
elif(month == 10):
    month1 = "October"
    days = 31
    
elif(month == 11):
    month1 = "November"
    days = 30
    
elif(month == 12):
    month1 = "December"
    days = 31

print("The entered month is" , month1, ", and the number of days in" , month1, "is", days)

    


    
    
