
print("Please enter the time you traveled in days, hours, minutes, and seconds.")

days = int(input("days"))

hours = int(input("hours"))

minutes = int(input("minutes"))

seconds = int(input("seconds"))

total = seconds + \
        (minutes * 60) + \
        (hours * 3600) +\
        (days * 86400)

print(days, "days", \
      hours, "hours", \
      minutes, "minutes", \
      seconds, "seconds are", \
      total, "seconds")
