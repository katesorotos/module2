# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:10:30 2018

@author: Kate Sorotos
"""
import time

class Customer(object):

    """A customer of ABC Bank with a checking account. Customers have the following properties:
 Attributes:
 name: A string representing the customer's name.
 balance: A float tracking the current balance of the customer's account.
 """
#'self' is an undefined placeholder for object i.e 'customer 1' 
#__init__ tells class what properties it should have/object's attributes/specifies data attributes
#default arguments i.e 'balance=0.0' must be declared at the end
 
    def __init__(self, name, surname, balance=0.0, age=0):       
        """Return a Customer object whose name is *name* and starting  balance is *balance*."""        
        self.name = name      
        self.surname = surname
        self.balance = balance
        self.age = age
        
#aboove variables used as input for function below        
#'name', 'balance' 'age' and 'surnname' act as placeholders

#withdraw amount = input 
#new balance = output        
    def withdraw(self, withdrawAmount):        
        """Return the balance remaining after withdrawing *amount* dollars."""       
        if withdrawAmount > self.balance:            
            raise RuntimeError('Amount greater than available balance.')
        else:
            self.balance -= withdrawAmount        
        return self.balance
    def deposit(self, amount):       
        """Return the balance remaining after depositing *amount* dollars."""       
        self.balance += amount        
        return self.balance 
    
#object id = class name(attributes/values belonging to object/properties relating to object (dependednt on __init__))
        
customer1 = Customer('Kate', 'Sorotos', 1000.0, 23)
withdrawAmount = float(input("How much would you like to withdraw today? £"))
print("£", withdrawAmount)
print("New balance:",customer1.balance-withdrawAmount)
time.sleep(2)
print("Would you like to use another service? y/n")

#inheritance
class Animal():
    def __init__(self, name, age=0.0):
        self.name = name
        self.age = age 
    def eat(self):
        print('yum!')
        
class Dog(Animal):
    def __init__(self, name, age=0.0, barkNumber = 0):
        self.name = name
        self.barkNumber = barkNumber
        self.age = age
        
    def bark(self):
        print('Woof! '*self.barkNumber)
        
class Boxer(Dog):
    def __init__(self, name, colour, age=0.0, walks = 0, barkNumber = 0):
        Dog.__init__(self, name, age=0.0, barkNumber = 0)
#       self.name = name
#       self.barkNumber = barkNumber
#       self.age = age
        self.colour = colour
        self.walks = walks
        #updates barkNumber to value input by user
    def updateBark(self, barkNumberinput):
        self.barkNumber = barkNumberinput
        return barkNumberinput
            
    def detectBark(self):
        if self.barkNumber >=3:
            print("Your dog wants a walk")
        else:
            print("Maybe your dog wants food")
                
class Cat(Animal):
    def __init__(self, name, colour, age=0.0, meowNumber = 0):
        self.name = name
        self.age = age   
    def meow(self):
        print('Meow')
        
#dog(animal)
Snoopy = Dog()
Snoopy.bark()
Snoopy.eat()

#boxer(dog)
#
#boxer1.eat()
#boxer1.bark()
#print(boxer1.age)
#print(boxer1.name)
        

name = input("What is your dog's name? ")
colour = input("What colour is your dog? ")
age = int(input("What is your dog's age? "))
walks = int(input("How many walks does it need a day? "))
barkNumber = int(input("How many times a day does your dog bark? "))

boxer1 = Boxer(name, age, colour, barkNumber, walks)

print(boxer1.updateBark(barkNumber))

boxer1.detectBark()

cat(animal)
cat1 = Cat('Daisy', 14)
print(cat1.name)
cat1.meow()



###########################

#class Robot():
#    def move(self):
#        print('... move move move...')
#class CleanRobot(Robot):
#    def clean(self):
#        print('I vacuum dust')
#class CookRobot(Robot):
#    def cook(self):
#        print("I'm a robot that likes to cook")
#class PizzaRobot(CookRobot):
#    def pizza(self):
#        print("I cook the best pizza!!)
 
#############################

##Chen's code       
#class Animal():
#    def __init__(self, name, age=0):
#        self.name = name
#        
#    def eat(self):
#         print('yum')
#         
#class Dog(Animal):
#    def __init__(self, name, age=0,barkNumber=0):
#        self.barkNumber = barkNumber
#        
#    def bark(self):
#        print('Woof! '*self.barkNumber)
#        
#        
#class Boxer(Dog):
#    def detect(self):
#        if self.barkNumber>=3:
#            print('strenger coming!!!')
#        
#        
#name = input('what is your pet\'s name:')        
#age = int(input('what is your pet\'s age: '))
#bark = int(input('how many times you heard it barked: '))
#
#dog007 = DogAgent(name, age, bark) #always inheritant ancester's
#dog007.bark()
#dog007.eat()
#dog007.detect()

##############################
#association - conposition 
#including objetcs from other classes

class Animal(): #superclass
    def eat(self):
         print('yum')
         
class Dog(Animal): #subclass of Animal
    def bark(self):
        print('Woof!')
class Robot(): #superclass
    def move(self):
        print('... move move move...')
class CleanRobot(Robot):  #subclass of Robot
    def clean(self):
        print('I vacuum dust')
        
class SuperRobot(): #includes objects from above classes 
    def __init__(self):
        self.o1 = Robot() #object from other class
        self.o2 = Dog() #object from other class, also inherit from animal class
        self.o3 = CleanRobot() #object from other class
    def playGame(self):
        print('AlphaGo Game')
    def move(self): #inlcuded from Robot
        return self.o1.move()
    def bark(self): #included from Dog
        return self.o2.bark()
    def eat(self): #included from Dog(Animal)
        return self.o2.eat()
    def clean(self): #included from CleanRobot
        return self.o3.clean()

machineDog = SuperRobot()
machineDog.move()
machineDog.bark()
machineDog.clean()
machineDog.eat()
machineDog.playGame()
