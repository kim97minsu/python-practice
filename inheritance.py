# Inheritance "is a"
# Composition "has a"
# Interface "does a"

# Bank Account 
#   -> checking account 
#   -> savings account

# Base Class
# class Car:
#     # Constructor 
#     def __init__(self, position):
#         # Car has a position 
#         self.position = position
#         # Car has a constant speed
#         self.speed = 10
        
#     # Car can move its position based on speed    
#     def move(self):
#         self.position += self.speed    
    
#     # Car can honk
#     def honk(self):
#         print("honk honk")

# # Bus class INHERITS from Car class
# class Bus(Car):
#     # Constructor
#     def __init__(self, position):
#         # Call the constructor of the parent class
#         super().__init__(position) # super is car, therefore Car.__init__ etc..
#         # Add a new attribute, passengers, specific to Busses
#         self.passengers = []
        
#     # Add a new method, add_passengers, specific to Busses
#     def add_passenger(self, name):
#         self.passengers.append(name)

# # Create a new Bus instance
# brocks_bus = Bus(0) # 0 is the starting position
# # Bus inherits from Car and can call Car's methods 
# brocks_bus.honk()
# # Bus has its own methods 
# brocks_bus.add_passenger("Tyler")
# print(brocks_bus.passengers)

# brocks_car = Car(0)
# brocks_car.move()    
# brocks_car.move()    
# brocks_car.honk()    
# brocks_car.honk() 
# print(brocks_car.position)   






class Phone:
    def __init__(self, number):
        self.number = number 
     
    def call(self, number):
        print(self.number + " is calling " + number)

class SmartPhone(Phone):
    def __init__(self, number):
        super().__init__(number)
    
    def textmsg(self, number):
        print(self.number + " is texting " + number)


class IPhone(SmartPhone):
    def __init__(self, number):
        super().__init__(number)

    def text(self, number):
        print(self.number + " is sending an iMessage " + number)
        
minsu_smartphone = SmartPhone("(911) 911-9911")
minsu_smartphone.textmsg("777 7777")
minsu_smartphone.call("777 7777")

todds_iphone = IPhone("123 1234")
todds_iphone.text(minsu_smartphone.number)