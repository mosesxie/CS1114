xCoordinate = int(input("Enter a non-zero number for the X-Coordinate: "))

yCoordinate = int(input("Enter a non-zero number for the Y-Coordinate: "))

if xCoordinate > 0 and yCoordinate > 0:
    print("The point is in the first quadrant")

elif xCoordinate < 0 and yCoordinate > 0:
    print("The point is in the second quadrant")

elif xCoordinate < 0 and yCoordinate < 0:
    print("The point is in the third quadrant")

else:
    print("The point is in the fourth quardrant")
    
