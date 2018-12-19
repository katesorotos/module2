# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:29:27 2018

@author: Kate Sorotos
"""

"""Revising classes"""
 
#Initialising the person class
class Person:
    def __init__(self, firstName, secondName, age, gender):
        self.firstName = firstName
        self.secondName = secondName
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else: 
            print('Gender not recognised!')
    def greetingInformal(self):
        print('Hi', self.firstName)
    def greetingFormal(self):
        if self.isMale:
            print('Welcome, Mr', self.firstName)
        else: 
            print('Welcome, Ms', self.secondName)
    def greetingAgeBased(self):
        if self.age < 18:
            print('Welcome, young ', self.firstName)
        elif self.age > 25:
            print('Welcome, venerable ', self.firstName)
        else:
            self.greetingFormal()
            
class Wizard(Person):
    def __init__(self, firstName, secondName, age, gender):
        Person.__init__(self, firstName, secondName, age, 'm')
    def spell(self):
        print('Expelliarmus!')
    def greetingFFormal(self):
        print('Welcome, Mr ', self.name, end=' ')
        print('- you\'re a fine Wizard!')
            
#Creating an instance/object
p1 = Person('Kate', 'Sorotos', 23, 'f')
p1.firstName #'Kate'
p1.age #'23'
p1.isMale #'False'
p1.greetingInformal #'Hi Kate'
p1.greetingFormal() #'Welcome, Ms Kate'

#Creating further instances/objects
p2 = Person('Mia', 'Egle', 5, 'f')
p3 = Person('Henri', 'Sorotos', 25, 'm')



