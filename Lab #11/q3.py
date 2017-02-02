def sumColumn(filename):

    f = open(filename, 'r', encoding="UTF-8")

    sumofnumbers = 0

    for i in range(5):

        x = int(f.readline())

        sumofnumbers += x

    return sumofnumbers
        

    f.close()

def main():

    p = sumColumn("q2.txt")

    print(p)

main()
