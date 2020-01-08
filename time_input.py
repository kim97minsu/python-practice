# Assume the user gives consistent input
# Example times include '05:45 PM' and '12:18 AM'
# time = input("What time is it? ")
# Parse hour, minute and AM/PM from 'time'
# Review List Slicing in Python!
# Print if time is before 08:00 AM
#   print("I am asleep! 🛌")
# Print if time is between 08:00 AM and 06:00 PM
#   print("I am busy 💻")
# Print if time is after 06:00 PM
#   print("Having fun 😎")


# import datetime
time = input("What time is it? ") # 9:00 AM

# Parse hour, minute and AM/PM from 'time'
hour = int(time[0:2])
minute = int(time[3:5])
period = time[6:8]

print(hour, minute, period)

if (hour < 8) and (period == 'AM'):
    print("I am asleep!")
elif (period == 'AM' and hour >=8) or (period =='PM' and hour < 6):
    print("I am busy!")
elif (hour >= 6) and (period =='PM'):
    print("I am having fun!")
# this doesn't work yet, convert it to 24 hours


