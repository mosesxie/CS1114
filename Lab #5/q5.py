import turtle

sides = int(input("Please enter an integer: "))

interiorAngle = (180 * (sides - 2)) / sides
exteriorAngle = 180 - interiorAngle

for currentSide in range(1, sides + 1):
    turtle.forward(100)
    turtle.left(exteriorAngle)

