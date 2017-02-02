# Moses Xie
# mx407
# hw8q2
#
# remove first word using find method 
# reverse function adds those words to a string in the opposite order and removes it from the phrase

def firstword(phrase):

    index = phrase.find(" ")

    word = phrase[:index]

    if index == -1:
        return phrase

    return word

def removefirstword(phrase):

    index = phrase.find(" ")

    if index == -1:
        return phrase

    newphrase = phrase[index + 1:]

    return newphrase

def reverse(phrase):

    counter = 0

    word = ""

    string = ""

    for character in phrase:

        if character == " ":

            counter += 1


    for i in range(0, counter + 1):

        word = firstword(phrase)

        string = word + " " + string 

        phrase = removefirstword(phrase)

    return string

def main():

    userPhrase = input("Enter a phrase: ")

    newPhrase = reverse(userPhrase)

    print(newPhrase)

main()
    

        

    
