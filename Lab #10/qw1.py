def mycount(lst, item):

    counter = 0

    for element in lst:

        if element == item:

            counter += 1


    return counter


def myindex(lst, item):

    for i in range(0, len(lst)):

        if lst[i] == item:

            return i


    return -1


def all_indices(lst, item):

    indices = []

    for i in range(0, len(lst)):

        if lst[i] == item:

            indices.append(i)

            
    if indices == []:
        return -1
    else:
        return indices


def remove_below_avg(lst):

    total = 0

    average = 0

    belowAverage = []

    for element in lst:

        total = total + element

    average = total / len(lst)

    for element in lst:

        if element > average:

            belowAverage.append(element)


    return belowAverage

def main():

    a = mycount([123, 'xyz', 'zara', 'abc', 123], 123)

    print(a)

    a = myindex([123, 'xyz', 'zara', 'abc', 123], 123)

    print(a)

    a = all_indices([123, 'xyz', 'zara', 'abc', 123], 123)

    print(a)

    a = remove_below_avg([2, 3, 5, 1, -4, 8, 0, -1])

    print(a)


main()

    

    





    
