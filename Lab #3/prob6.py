import turtle
import math
a = int(input("Please enter an integer between 50 and 500: "))

b = int(input("Please enter a different integer between 50 and 500: "))

turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(b)

midHeight = b / 2
midWidth = a / 2

innerLength = math.sqrt(midHeight**2 + midWidth**2)
radianA = math.atan(midWidth/midHeight)
radianB = math.atan(midHeight/midWidth)
angleA = math.degrees(radianA)
angleB = math.degrees(radianB)

print(angleB)

turtle.left(180)
turtle.forward(midHeight)
turtle.right(angleA)
turtle.forward(innerLength)
turtle.right(angleB * 2)
turtle.forward(innerLength)
turtle.right(angleA * 2)
turtle.forward(innerLength)
turtle.right(angleB * 2)
turtle.forward(innerLength)

