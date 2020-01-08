# Variables are scoped to functions
x = 12 # GLOBAL SCOPE 

def scoped_variable():
    y = 14 
    print(y)

# Name 'y is not avaiable outside of the function 
# print(y) # Error! 


# Same name, different scopes 
x = 12 

def set_x():
    # this 'x' is shadowing the 'x' in global
    x = 14 
    
set_x() # Create a new 'x'
print(x) # returns 12 because of global scope

# Change global name with function 
z = 9 

def increment_z():
    global z 
    z = z + 1
    
increment_z()

def create_incrementor(increment):
    def incrementor(number):
        return number + increment
    return incrementor
# Create a function that returns a function 
# That new function will increment a number by a value passed in to the orginal function 

# create_incrementor 
increment_by_1 = create_incrementor(1)
print(increment_by_1(10)) # returns 11 
increment_by_2 = create_incrementor(2)
print(increment_by_2(10)) # returns 12


# given these functions
def increment(n):
    return n + 1
def decrement(n):
    return n - 1

# Write a function that takes a number and a function, calling the passed-in function twice
def double(number, fn):
    return fn(fn(number))

print(double(12, increment)) # Return 14 
print(double(12, decrement)) # return 10

# Nested Function Scope 
name = "Brock"
def outer_function():
    def inner_function():
        global name
        name = "Tyler"
    inner_function()

outer_function()
print(name)

