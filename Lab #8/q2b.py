def find(some_string, substring, start, end):

    flag = False
    counter = 1
    match = 0

    for index in range(0, len(some_string)):

        if some_string[index] == substring[0]:
            
            
            x = index

            for index2 in range(1,len(substring)):
                
                x = x + 1
                

                if some_string[x] == substring[index2]:
                    counter +=1

                if counter == len(substring):
                    flag = True
                    print(index)

                if index2 == len(substring)-1:
                    counter = 1
                    

                    



def main():
    find("ACGCCTCGA", "CG", 0, 0)

main()
