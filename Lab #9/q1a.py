def count(lst, item):

    counter = 0

    for index in lst:

        if item == index:
            counter += 1

    return counter

def main():

    item = "0"

    lst = [0,32,"a","0","4","15","q","0"]

    counter = count(lst, item)

    print(counter)

main()

        
    
