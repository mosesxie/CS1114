a = int(input("Please enter a: "))

b = int(input("Please enter b: "))

if (a == 0 and b == 0):
    print("There are an infinte number of solutions. ")

elif (a == 0 and b != 0):
    print("No Solution")

else:
    x = -b/a
    print("The equation has a single solution and x = ", x)
