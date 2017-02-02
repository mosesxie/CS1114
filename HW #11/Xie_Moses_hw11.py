'''

Moses Xie
CS 1114
mx407

Manipulates data in a csv file to find clean data and calculate stats with this data
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    # Complete this function to clean the CSV.
    # It should create a new file as specified in the assignment specs.

    completeVersion = open(complete_weather_filename, 'r', encoding="UTF-8")

    cleanedVersion = open(cleaned_weather_filename, 'w', encoding="UTF-8")

    header_line1 = completeVersion.readline()
    header_line2 = completeVersion.readline()

    for line in completeVersion:

        line = line.rstrip()

        lineSplit = line.split(",")

        if len(lineSplit)>1:

            print(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[8], sep = ",", file = cleanedVersion)

        


        
        
    
    cleanedVersion.close()
    completeVersion.close()

# Part B

def f_to_c(f_temperature):

    if f_temperature.isdigit():

        f_temperature = int(f_temperature)

        c_temperature = (5/9) * (f_temperature-32)

        return c_temperature

    else:
        return f_temperature

def in_to_cm(inches):

    if inches.isdigit():

        inches = int(inches)

        centimeters = inches * 2.54

        return centimeters
    else:
        return inches


def convert_data_to_metric(imperial_weather_filename,metric_weather_filename):

    nonmetricVersion = open(imperial_weather_filename, 'r', encoding="UTF-8")

    metricVersion = open(metric_weather_filename, 'w', encoding="UTF-8")

    for line in nonmetricVersion:

        line = line.rstrip()

        lineSplit = line.split(',')

        lineSplit[2] = f_to_c(lineSplit[2])

        lineSplit[3] = f_to_c(lineSplit[3])

        lineSplit[4] = in_to_cm(lineSplit[4])

        print(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], sep = ",", file = metricVersion)

    metricVersion.close()

    nonmetricVersion.close()

# Part C
def print_average_temps_per_month(city,weather_filename, unit_type):

    weatherFile = open(weather_filename, 'r', encoding="UTF-8")

    highSums = [0] * 12

    lowSums = [0] * 12

    highAvg = [0] * 12

    lowAvg = [0] * 12

    counterList = [0] * 12

    monthsList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]



    for line in weatherFile:

        line = line.rstrip()

        lineSplit = line.split(",")

        dateSplit = lineSplit[1].split("/")


        if lineSplit[0] == city:


            highSums[int(dateSplit[0])-1] += float(lineSplit[2])

            lowSums[int(dateSplit[0])-1] += float(lineSplit[2])

            counterList[int(dateSplit[0])-1] += 1



    for month in range(0,12):

        print(monthsList[month])
        print(highSums[month]/counterList[month])
        print(lowSums[month]/counterList[month])

        print("\n")

#Part D finds the month with the highest rainfall in a city

def higher_rainfall_month(city1,weather_filename):

    weatherFile = open(weather_filename, 'r', encoding="UTF-8")

    highSums = [0] * 12

    lowSums = [0] * 12

    highAvg = [0] * 12

    lowAvg = [0] * 12

    counterList = [0] * 12

    monthsList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]



    for line in weatherFile:

        line = line.rstrip()

        lineSplit = line.split(",")

        dateSplit = lineSplit[1].split("/")


        if lineSplit[0] == city:


            highSums[int(dateSplit[0])-1] += float(lineSplit[2])

            lowSums[int(dateSplit[0])-1] += float(lineSplit[2])

            counterList[int(dateSplit[0])-1] += 1




            

    print("High Average", monthList[highAvg.index(max(highAvg))])

    print("Low Average", monthList[lowAvg.index(max(lowAvg))])

        

        



def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    higher_rainfall_month("San Francisco","weather in imperial.csv")



main()
