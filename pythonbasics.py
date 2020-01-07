import datetime
print('Current date/time: {}'.format(datetime.datetime.now()))

time = int(input("What time is it?"))
if time < 8:
    print("I am asleep! ")

elif time >= 8 and time <= 18:
    print("I am busy!")

elif time >= 18:
    print("I am having fun!")

# Get a random number
import random
random_number = random.randint(1, 10)
# Ask user to guess a number.
random_number = input()
guess = input("Guess a random number!")
# If their guess is too low, print "Too low!"
if random_number < guess:
    print("Too low!")
# If their guess is too high, print "Too high!"
if random_number > guess:
    print("Too high!")
# If their guess is wrong, ask for a number again.
if random_number == guess:
    print("You got it!")
# If their guess is correct, print "You got it!"

# Get month from user
current = input("Please type in a month. Ex: 'June' : ")

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# Calculate what month it will be nine months from now 
if 