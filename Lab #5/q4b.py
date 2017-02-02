userInt = int(input("Please eneter an integer:"))
3453

even = 0

odd = 0
while userInt != 0:
    currentDigit = userInt % 10
    userInt = userInt // 10
    if currentDigit % 2 == 0:
        even +=1
    else:
        odd +=1

print("Even =", even)
print("Odd =", odd)
        
