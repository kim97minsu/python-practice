# Default Parameters
def say_something(message):
    print(message)

say_something("Hello world!") # Prints "Hello world!"
# say_something() # Prints "Hello"

# def get_boats(id=None):
#     if id:
#         database.getById(id)
#     else: 
#         database.getAll()
        
# Specify parameters by name 
def greet_people(first_person, second_person):
    print("Hello " + first_person + " and " + second_person)
    
greet_people("Tyler", "Brock")
greet_people(first_person="Umar", second_person="Bruno") # Named parameters