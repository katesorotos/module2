# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:55:47 2018

@author: Kate Sorotos
"""

#user input


#print("What's your name?")
#name=input()
 
#name=input("What's your name? ")
#print("Hello {}!".format(name))

#print("Hello {}!".format(name)).upper() #makes everything upper
#print("Hello {}!".format(name.upper())) #makes name uppercase
#print("Hello {}!".format(name).title()) #makes first letter uppercase

#name=input("What’s your name? ")
#city=input("What’s your city? ")
#print("Hello {}! from {}".format(name.title(),city.title()))

#print("Where do you come from?")
#home=input("Where do you come from? ")
#print("Nice! I like {}!".format(home.title()))

#age=input("How old are you? ")
#print("Wow! I'm also {}!".format(age))

"""def hello_world():
    print("Hello World!")
        
hello_world()"""


def name():
    name=input("What's your name? ")
    print("Hello {}!".format(name.title()))
    #print(2+2)
    #print("Kate")
    number=int(input("Enter a number "))
    number_2=int(input("Enter another number "))
    #int(number)*int(number_2)
    multiply=number*number_2
    print("The sum of your numbers is {}!".format(multiply))
          
name()


"""def hello_world():
    print("Hello World!")
def name_surname():
    print("What's your name? ")
    name=input()
    
    print("My name is {}".format(name))
    addition()
def addition():
    add2_2=2+2
    print (add2_2)
    
name_surname()"""

