# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:22:50 2018

@author: Kate Sorotos
"""

import sys 

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
        

#boxer(dog)
#boxer1.eat()
#boxer1.bark()
#print(boxer1.age)
#print(boxer1.name)
        

name = sys.argv[1] #input("What is your dog's name? ")
colour = sys.argv[2] #input("What colour is your dog? ")
age = sys.argv[3] #int(input("What is your dog's age? "))
walks = sys.argv[4] #int(input("How many walks does it need a day? "))
barkNumber = sys.argv[5] #int(input("How many times a day does your dog bark? "))

boxer1 = Boxer(name, age, colour, barkNumber, walks)

print(name, colour, age, walks, barkNumber)

#print(boxer1.updateBark(barkNumber))


