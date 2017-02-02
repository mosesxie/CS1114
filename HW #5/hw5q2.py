n = int(input("Please enter a positive integer: "))

hourglass = ""

line = ""

a = 3

for i in range(1, n+1):
    if i == 1:
        line = " " * (n - i) + "*" + " " * (n - i) + "\n"
        hourglass = line + hourglass + line

    else:
        line = " " * (n - i) + "*" * a + " " * (n - i) + "\n"
        hourglass = line + hourglass + line
        a += 2

print(hourglass)
