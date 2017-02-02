def myfunc():

    try:
        x = int(input("Enter an first integer: "))

        y = int(input("Enter an first integer: "))

        print(x/y)

    except ZeroDivisionError:

        print("Infinity ")

    except ValueError:

        print("Input must be numbers")

myfunc()
