def fibonacci (n):
    num1 = 0
    sub = 0
    num2 = 1
    sub2 = 1

    if n == 1:
        return 0

    if n == 2:
        return 1

    for digit in range (1,n-1):
        
        if digit == 1:
            print("0")
        
        sub2 = num2
        num2 = num1 + num2
        num1 = sub2
        print(num1)

    print(num2)        
    

def main():

    number = int(input("Please enter a number: "))

    fibonacci(number)

main()

        
