def writeName(filename, firstName, lastName):

    f = open(filename, 'w', encoding="UTF-8")

    f.write(firstName + " " + lastName)

    f.close()

def main():

    writeName("filename.txt", "Moses", "Xie")

main()

    
