def add_entry(phonebook,name,phonenumber):

    if not(name in phonebook) and valid(phonenumber):

        phonebook[name] = phonenumber

    else:

        print(name,"Entry is invalid")

def valid(phonenumber):

    flag = True

    if phonenumber.isdigit() and len(phonenumber) == 10:

        flag = True

    else:
        flag = False


    return flag

def lookup(phonebook, name):

    try:

        return phonebook[name]

    except KeyError:

        print("name is not found")

def print_all(phonebook):

    print(phonebook)

def main():

    in_file = open("Lab12-phonebook.txt","r")

    phonebook = {}

    for line in in_file:

        line = line.rstrip()

        firstSpace = line.find(" ")

        secondSpace = line.find(" ", firstSpace + 1)

        add_entry(phonebook,line[0:secondSpace],line[secondSpace+1:])

    print(phonebook)
        

        

        

    in_file.close()

main()








    

        

                        
