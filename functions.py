# # Create function 
# def cool_function():
#     return "Hello, world!"
# # Call function
# cool_function() # Returns "Hello, world!"

# # Cretae function w/ arguments 
# def add(a,b):
#     return a + b 
# add(2, 3) # Returns 5

# # Function that does nothing 
# def do_nothing():
#     pass # nothing happens
# do_nothing() # Returns None

# # Write a function that takes a list of numbers and find the largest number
# def largest_number(list):
#     list.sort()
#     print("Largest element is:", list[-1]) 
# largest_number([3, 1, 5, 66, 2, 9, 4, 7, 8])

# # Even better
# def find_highest_value(numbers):
#     compare = 0
#     for number in numbers:
#         if number > compare: 
#             compare = number
#     return compare


                #### W3RESOURCES 20 PYTHON QUESTIONS ####
                
# print_this = find_highest_value([1,2,3,4,5,6,99])
# print(print_this)

# my answer: 
# Write a function to find the Max of three numbers
# array = [2,7,5]
# def max_three_numbers(numbers):
#     print(max(numbers)) # max()
# max_three_numbers(array)

# website answer 
# def max_of_two(x, y):
#     if x > y: 
#         return x
#     return y
# def max_of_three(x, y, z):
#     return max_of_two(x, max_of_two(y, z))
# print(max_of_three(3, 6, -5))

# Write a function to sum all the numbers in a list
array = [1,2,3,4]

def sum(numbers):
    total = 0 # make sure to initialize when add total 
    for i in numbers:
        total += i # increment 
    return total 
print(sum(array))

# Write a Python function to multiply all the numbers in a list
def multiply(numbers):
    total = 1 
    for i in numbers: 
        total *= i
    return total 
print(multiply([2,2,2]))

# Write a Python program to reverse a string
def reverse_string(string):
    reversed = ''
    index = len(string)
    while index > 0: 
        reversed += string[index - 1]
        index = index - 1
    return reversed
print(reverse_string('lmaoo'))