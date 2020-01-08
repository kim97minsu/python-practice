# Get a random number

# Get a random number
import random
random_number = random.randint(1, 100)

guess = None
# If their guess is wrong, ask for a number again.
while guess != random_number:
    # Ask user to guess a number.
    guess = int(input("Guess a number! "))
    # If their guess is too low, print "Too low!"
    if guess < random_number:
        print("Too low!")
    # If their guess is too high, print "Too high!"
    elif guess > random_number:
        print("Too high!")
    # If their guess is correct, print "You got it!"

print("You got it!")

