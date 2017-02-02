def get_Common_Ele(list1, list2):

    list3 = []

    for index1 in range(0, len(list1)):

        for index2 in range(0, len(list2)):

            if list2[index2] == list1[index1]:

                list3.append(list2[index2])

                list2[index2] = "0000"


    return list3

def main():

    list1 = [ 2, 'S', 3.13, 3.13, "Python" ]

    list2 = [ "Pythy", 2, 12, "hello", 3.13 ]

    list3 = get_Common_Ele(list1,list2)

    print(list3)

main()
