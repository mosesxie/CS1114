def circular_shift_list1(lst,k):

    lst2 = []

    place = -k    

    for index in range(0,len(lst)):

        lst2.append(lst[place])

        place +=1

    return lst2



def main():

    lst2 = circular_shift_list1([1,2,3,4,5,6,7,8],3)

    print(lst2)

main()
