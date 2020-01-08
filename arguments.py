# # Named Parameters

# # Default Parameters
# def divide(numerator, denominator):
#     return numerator // denominator

# print(divide(denominator=5, numerator=10))

# # Args 

# def do_something(*fancy_parameter):
#     print(fancy_parameter)
#     print(*fancy_parameter)
# do_something("first", "second", "third")

# def do_something(*words):
#     for word in words:
#         print(word)
# do_something("first", "second", "third")

# # kwargs
# def do_something_else(**fancy_parameter):
#     print(fancy_parameter)
    
# do_something_else(first="1", second="2", third="3")

# # Args 'n' Kwargs
# def do_another_thing(*args, **kwargs):
#     print(args)
#     print(kwargs)
    
# do_another_thing("first", "second", third="3", fourth="4")

# Can't have a parameter without a default value after parameters with defaults 
# def do_another_something(first, second, third=3, fourth=4, fifth):
#   pass

# Write a function that totals the numbers inside of a list 
# Or, subtract the values if an optional "subtract" boolean is passed in

# def total(numbers, do_subtraction=False): 
#     total = 0 # initialize it 
#     if do_subtraction:
#         for number in numbers:
#             total -= number
#     else:
#         for number in numbers:
#             total += number
#     return total 

# total([1,2,3])
# print(total([1,2,3], True))

# Decorators 
def outer_function(fn):
    def inner_function():
        fn()
    return inner_function

@outer_function
def say_hello():
    print("Hello, world")
    
say_hello()