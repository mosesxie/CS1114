currentPopulation = 307357870

currentYear = 2015

userYear = int(input("Enter an integer year: "))

yearlyBirth = (1/7) * 60 * 60 * 24 * 365 

yearlyDeath = (1/13) * 60 * 60 * 24 * 365 * -1

yearlyImmigrant = (1/35) * 60 * 60 * 24 * 365

yearlyChange = yearlyBirth + yearlyDeath + yearlyImmigrant

yearDifference = userYear - currentYear

populationChange = yearDifference * yearlyChange

yearPopulation = currentPopulation + populationChange

roundedPopulation = round(yearPopulation, 0)

print("Estimated Population of", userYear, "is:", roundedPopulation)
