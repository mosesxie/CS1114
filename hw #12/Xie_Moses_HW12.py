#Moses Xie
# mx407
#
#creates a dictionary with train line as the key and a list with the stop as the value
#




# takes user input and uses the other methods
def main():

    traindic = input_into_dictionary("train stop data-Mac.csv")

    userTrain = ""

    while userTrain != "done":

        userTrain = input("Please enter a train line, or 'done' to stop: ")

        if userTrain == "done":

            break

        print_trainline(userTrain, traindic)


# takes the file with data to create a dictionary of the train lines and stops
def input_into_dictionary(trainFile):

    in_file = open(trainFile,'r')

    dic = {}

    for line in in_file:

        line = line.rstrip()

        lineSplit = line.split(",")

        if lineSplit[0][0] in dic:

            if lineSplit[2] not in dic[lineSplit[0][0]]:

                dic[lineSplit[0][0]].append(lineSplit[2])
        else:

            dic[lineSplit[0][0]] = [lineSplit[2]]


    return dic

    

# prints the line and stops using an inputed line and the dictionary
def print_trainline(trainLine, traindic):

    output = trainLine + " train: "

    for stop in traindic[trainLine]:

        output += "  " + stop

    print(output)

main()
