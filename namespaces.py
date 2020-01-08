# Object-Oriented Programming

class Tyler:
    first = "Tyler"
    last = "Lane"
    age = 28
    
print(Tyler.first)
print(Tyler.last) # first and last are in the global scope but they are still in namespace for Tyler class

# Write a function that adds two numbers together called "add"
# This function should be in a "Calculator" namespace
# Call the add function from outside the Calculator namespace

class Calculator: 
    def add(self, b):
        return self + b
    def subtract(self, b):
        return self - b
print(Calculator.add(2,2))

# Procedural = data structures, processes
