# Moses Xie
# mx407
# hw8q1
#
# creates a month using a for loop
# yearly claendar uses the calendar function recursivly for 12 months
def calendar(daysMonth, dayWeek):

    print("Mo \t Tu \t We \t Th \t Fr \t Sa \t Su \n")

    string = ""

    counter = 1

    p = 1

    for day in range(0, daysMonth + dayWeek):

        p += 1

        if day < dayWeek:

            string = string + "   \t"

        else:

            string = string + str(counter) + "\t"
            counter +=1

        if day % 7 == 0:

            string = string + "\n"

            p = 1

    string = string + "\n \n"


    print(string)


    return p


def leapyear(year):

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):

        return True

    else:
        return False


def yearlycalendar(year, dayofweek):

    leap = leapyear(year)

    print("Jan")

    f = calendar(31, dayofweek)

    
    print("Feb")

    if leap:

        g = calendar(29, f)

    else:
        g = calendar(28, f)

    print("Mar")

    h = calendar(31, g)

    print("Apr")
    
    i = calendar(30, h)

    print("May")

    j = calendar(31, i)

    print("June")

    k = calendar(30, j)

    print("July")

    l = calendar(31, k)

    print("August")

    m = calendar(31, l)

    print("Sep")

    n = calendar(30, m)

    print("Oct")

    o = calendar(31, n)

    print("Nov")

    p = calendar(30, o)

    print("Dec")

    q = calendar(31, p)


    

def main():

    a = int(input("Enter the year: "))

    b = int(input("Enter the first day of the first month: "))

    yearlycalendar(a,b)

    

main()
    

    




            

    
