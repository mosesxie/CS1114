def find_min_index(lst):

    minimum = min(lst)

    for index in range(0, len(lst)):

        if lst[index] == minimum:

            return index 

        

def main():

    index = find_min_index([56,24,58,10,33,95])

    print(index)

main()
    
