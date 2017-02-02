import random

def create_permutation(lst):

    x = len(lst)

    permutatedList = []

    for i in range(x):

        element = lst.pop(random.randint(0,len(lst)-1))

        permutatedList.append(element)

    return permutatedList

def main_q1():

    integer = int(input("Enter an integer: "))

    lst = []

    for i in range(integer):

        lst.append(i)

    newList = create_permutation(lst)

    print(newList)

def add_list(lst1, lst2):

    sumList = []


    for i in range(0,len(lst1)):

        x = lst1[i] + lst2[i]

        sumList.append(x)

    return sumList

def main_q2():

    element = ""

    element2 = ""

    lst1 = []

    lst2 = []

    while element != "done":

        element = input("Enter a number for list 1: ")

        if element != "done":

            lst1.append(int(element))

    while element2 != "done":

        element2 = input("Enter a number for list 2: ")

        if element2 != "done":

            lst2.append(int(element2))

    finalList = add_list(lst1,lst2)

    print(finalList)

def create_prefix_lists(lst):

    finalList = []

    for i in range(len(lst) + 1):

        finalList.append(lst[0:i])

    return finalList

def main_q3():

    x = create_prefix_lists([2,4,6,8,10])

    print(x)


def read_menu():

    itemAmount = int(input("How many items are on the menu: "))

    itemList = []

    for i in range(itemAmount):

        itemInfo = input("Enter item in the form (name:price)")

        item = itemInfo.split(":")

        item[1] = float(item[1])
        
        itemList.append(tuple(item))


    return itemList

def read_customer_order():

    print("What would you like to order? ")

    orderList = []

    item = ""

    while item != "done":

        item = input()

        if item != "done":

            orderList.append(item)

    return orderList

def compute_price(menu_list, order_list):

    totalPrice = 0

    for orderItem in order_list:

        for menuItem in menu_list:

            if orderItem == menuItem[0]:

                totalPrice += menuItem[1]

    return totalPrice

def main():

    menu = read_menu()

    for i in range(0,3):

        order = read_customer_order()

        initialPrice = compute_price(menu,order)

        totalPrice = initialPrice + (initialPrice * 0.0085) + (initialPrice * 0.15)

        roundedtotalPrice = round(totalPrice, 2)

        print("Your Price is", roundedtotalPrice)

main()

    

            
        

        
    








        

    

        

    

        

        
