def max_abs_val(lst):

    absolutevaluelist = []

    for element in lst:

        if element < 0:

            absolutevaluelist.append(element * -1)

        else:

            absolutevaluelist.append(element)

    

    maxValue = max(absolutevaluelist)

    return maxValue

def main_q1():

    x = max_abs_val([-19, -3, 20, -1, 0, -25])

    print(x)

def find_all (lst,val):

    indexes = []

    for i in range(len(lst)):

        if lst[i] == val:

            indexes.append(i)

    return indexes

def main_q2():

    x = find_all(['a', 'b', 10, 'bb', 'a'], "a")
    print(x)


def reverse1(lst):

    
    lst2 = []

    place = -1  

    for index in range(0,len(lst)):

        lst2.append(lst[place])

        place -=1

    return lst2

def reverse2(lst):

    lst2 = []

    place = -1

    for index in range(0,len(lst)):

        lst2.append(lst[place])

        place -=1

    lst = lst2

    return lst

    

def main_q3():

    lst1 = [1, 2, 3, 4, 5, 6]

    rev_lst1 = reverse1(lst1)

    print(rev_lst1)

    lst2 = [1,2,3,4,5,6]

    rev_lst2 = reverse2(lst2)

    print(rev_lst2)


def encoder(input_str):

    current_position = 0

    second_counter = 1

    lst = []

    print_str = "Your string has: \n"

    while current_position < len(input_str):
        flag = input_str[current_position]
        counter = 0
        while(flag == input_str[current_position]):
        
            counter += 1
            current_position += 1
            if current_position == len(input_str):
                break

        lst.append([flag,counter])

    return lst

def decoder(lst):

    decodedString  = ""

    for element in lst:

        decodedString = decodedString + element[0] * (element[1])

    return decodedString

def main_q4():

    x = encoder("supercalifragilisticexpialidocious")

    print(x)

    y = decoder(x)

    print(y)

main_q4()



    

    


    

    
