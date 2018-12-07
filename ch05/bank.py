# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:56:21 2018

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