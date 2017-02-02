userExpression = input("Enter a mathematical expression: ")

spaceIndex1 = userExpression.find(" ")

spaceIndex2 = userExpression.find(" ", spaceIndex1 + 1)

firstNumber = int(userExpression[:spaceIndex1])

secondNumber = int(userExpression[spaceIndex2 + 1:])

if userExpression[spaceIndex1 + 1: spaceIndex2] == "+":
    answer = firstNumber + secondNumber

if userExpression[spaceIndex1 + 1: spaceIndex2] == "-":
    answer = firstNumber - secondNumber


if userExpression[spaceIndex1 + 1: spaceIndex2] == "*":
    answer = firstNumber * secondNumber


if userExpression[spaceIndex1 + 1: spaceIndex2] == "/":
    answer = firstNumber / secondNumber

print(answer)


