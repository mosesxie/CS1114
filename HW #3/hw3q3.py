import math

a = int(input("Please enter value of a: "))

b = int(input("Please enter value of b: "))

c = int(input("Please enter value of c: "))


if ((b**2)-4 * a * c) < 0:
    print("There are no real solutions")

elif (a == 0 and b == 0 and c == 0):
    print("There are an infinite number of solutions: ")

elif(a == 0 and b == 0 and c != 0):
    print("There are no solutions")

else:
    positiveX = ((-b + math.sqrt((b**2)-4 * a * c)) / (2 * a))

    negativeX = ((-b - math.sqrt((b**2)-4 * a * c)) / (2 * a))

    if (positiveX == negativeX):
        print("There is one solution:", positiveX)
    else:
        print("There are two solutions", postiveX, "and". negativeX)






