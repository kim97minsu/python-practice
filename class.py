class Library:
    # Dunder Init, our constructor method
    # Requires "self" parameter
    # Python's version of "this"
    def __init__(self, books, city):
        # assigned to self.books and books is the parameter being passed in to dunder init
        self.books = books
        self.city = city
    def is_in_collection(self, book_to_find):
        for book in self.books:
            if book == book_to_find:
                return True
            return False 
    # def say_hello():
    #     print("Hello") # Python will error this out because there are no parameters, unlike JavaScript
    
# Create instances of the Library class
tylers_library = Library(['To Kill a Mockingbird', 'Moby Dick'], 'Austin')
brocks_library = Library(["Beginner's Game"], 'Toronto')

# Iterate over data in object instance
for book in tylers_library.books:
    print(book)
print(tylers_library.city)

# Call a method 
# The following two lines are doing the exact same thing 
# Library.is_in_collection(tylers_library, 'The Taking Tree')
tylers_library.is_in_collection('The Taking Tree')

# Non-instance functions can be called as properties of the namespace
# Library.say_hello()
# Methods will always pass in 'self' and throw an error if not given 
# tylers_library.say_hello()



# Make a Bank Account class
#   What data?
#   What procedures

class Bank_Account:
    def __init__(self, starting_balance):
        self.balance = starting_balance
    
    def deposit(self, amount):
        self.balance += amount
        self.check_balance()
                
    def withdraw(self, amount):
        if self.has_enough_money_for(amount):
            self.balance -= amount
        else: 
            return False
    
    def has_enough_money_for(self, amount):
        return self.balance > amount
    
    def transfer(self, other_account, amount):
        if self.has_enough_money_for(amount):
            self.balance - amount
            other_account.balance + amount
            return True
        else: 
            return False
                        
minsus_account = Bank_Account(5000)
brunos_account = Bank_Account(1000)
minsus_account.deposit(100)

minsus_account.check_balance()
minsus_account.transfer(brunos_account, 50)
