birthDate = int(input("Please enter a date of birth: "))

currentDate = int(input("Please enter today's date: "))

yearBirth = birthDate // 10000

remainingBMonth = birthDate % 10000

yearCurrent = currentDate // 10000

remainingCMonth = currentDate % 10000

ageYear = yearCurrent - yearBirth

monthBirth = remainingBMonth // 100

remainingBDays = remainingBMonth % 100

monthCurrent = remainingCMonth // 100

remainingCDays = remainingCMonth % 100

ageMonth = monthCurrent - monthBirth

ageDays = remainingCDays - remainingBDays

print("You are", ageYear, "years", ageMonth, "months and", ageDays, "days old.")


