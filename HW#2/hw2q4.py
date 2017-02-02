daysJohn = int(input("Please enter the number of days John has worked: "))

hoursJohn = int(input("Please enter the number of hours John has worked: "))

minutesJohn = int(input("Please enter the number of minutes John has worked: "))

daysBill = int(input("Please enter the number of days Bill has worked: "))

hoursBill = int(input("Please enter the number of hours Bill has worked: "))

minutesBill = int(input("Please enter the number of minutes Bill has worked: "))

totalJohn = (daysJohn * 60 * 24) + (hoursJohn * 60) + minutesJohn

totalBill = (daysBill * 60 * 24) + (hoursBill * 60) + minutesBill

total = totalJohn + totalBill

daysSum = total // 1440

remainingTotal = total % 1440

hoursSum = remainingTotal // 60

remainingTotal = remainingTotal % 60

minutesSum = remainingTotal

print("The total time both of them worked together is:" , daysSum, "days", hoursSum, "hours and", minutesSum, "minutes.")
