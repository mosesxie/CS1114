import turtle

color = input("PLease enter a color: ")

shape = input("PLease enter a shape: ")

size = int(input("PLease enter a size number: "))

turtle.color(color)

counter = 0

if (shape == "triangle"):
    sides = 3
    angle = 60

elif (shape == "square"):
    sides = 4
    angle = 90

elif(shape == "pentagon"):
    sides = 5 
    angle = 108

else:
    print("The shape is invalid")

while sides > counter:
    turtle.forward(size)

    turtle.left(180-angle)

    counter = counter + 1
