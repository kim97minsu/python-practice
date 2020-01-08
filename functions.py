# Create function 
def cool_function():
    return "Hello, world!"
# Call function
cool_function() # Returns "Hello, world!"

# Cretae function w/ arguments 
def add(a,b):
    return a + b 
add(2, 3) # Returns 5

# Function that does nothing 
def do_nothing():
    pass
do_nothing() # Returns None

# Write a function that takes a list of numbers and find the largest number
def largest_number(list):
    list.sort()
    print("Largest element is:", list[-1]) 
largest_number([3, 1, 5, 66, 2, 9, 4, 7, 8])

def find_highest_value(numbers):
    compare = 0
    for number in numbers:
        if number > compare: 
            compare = number
    return compare

