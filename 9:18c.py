import math

radius = int(input("Please enter an integer for radius: "))

circumference = 2 * math.pi * radius

roundedC = round(circumference,2)

area = math.pi * radius ** 2

roundedA = round(area, 2)

print("Circumference of the circle is:", roundedC, "and area of circle is:", roundedA)
