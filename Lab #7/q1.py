input_str = input("Please enter a string of 0s and 1s: ")

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
        
        
    print_str = print_str + str(counter) + " " + flag + "'s \n"


print(print_str)
    
