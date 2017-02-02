import random

def writeRandNumbers(filename, n):

    f = open(filename, 'w', encoding="UTF-8")

    for i in range(n):

        x = random.randint(1,100)

        f.write(str(x) + "\n")

        

    f.close()

def main():

    writeRandNumbers("q2.txt", 5)

main()
