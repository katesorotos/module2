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


"""def name():
    name=input("What's your name? ")
    print("Hello {}!".format(name.title()))
    #print(2+2)
    #print("Kate")
    number=int(input("Enter a number "))
    number_2=int(input("Enter another number "))
    #int(number)*int(number_2)
    multiply=number*number_2
    print("The sum of your numbers is {}!".format(multiply))
          
name()"""


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

def hello_world_2args(a, b):
    print ("{} {}".format(a,b))

a1='hello'
b1='world'
a2='love'
b2='coding'
hello_world_2args(a1, b1)
hello_world_2args(a2, b2)

print() 

def hello_world_5args(a, b, c, d, e):
    print("{} {} {} {} {}".format(a,b,c,d, e))
    
a1='Hey'
b1='world!'
c1='Are'
d1='You'
e1='ready?'
a2='Lets'
b2='do'
c2='some'
d2='fun'
e2='coding!'

hello_world_5args(a1,b1,c1,d1, e1)
hello_world_5args(a2,b2,c2,d2, e2)

print()

print (range (10))
print (range (1,10)) 
print (range (1,10,2)) 

print()

def add_two_numbers():
 number1 = 100
 number2 = 200
 answer = number1 + number2
 print ("{} plus {} is {}".format(number1, number2, answer))

add_two_numbers()

print()

def add_two_numbers_from_args(number1, number2): 
 answer = number1 + number2
 print ("{} plus {} is {}".format(number1, number2, answer))

add_two_numbers_from_args(5,10) 

print()
#
#def multiply_two_numbers():
#    number=int(input("Enter a number "))
#    number_2=int(input("Enter another number "))
#    multiply=number*number_2
#    print("{} multiplied by {} = {}!".format(number, number_2, multiply))
#
#multiply_two_numbers()


print()

def convert_distance(miles): 
    kilometers = (miles * 8.0) / 5.0 
   # print ("Converting distance in miles to kilometers:") 
    return(kilometers)
    #print ("Distance in miles:", miles) 
    #print ("Distance in kilometers:", kilometers)
    returned_value = convert_distance(miles)
    print(returned_value)
    
convert_distance(34)

print() 

#def convert_temp(centigrade):
#    fahrenheit = centigrade * 9.0 / 5.0 + 32 
#    kelvin = centigrade + 273.15
#    print("That's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit, kelvin))
#centigrade = float(input("What's the temperature where you are today? "))
#convert_temp(centigrade)
#    
#    print('Converting temperature in centigrade to fahrenheit and kelvin:')
#    print('Temperature in centigrade:', centigrade)
#    print('Temperature in fahrenheit:', fahrenheit)
#    print('Temperature in kelvin:', kelvin)
    
#convert_temp()

def add_two_numbers_and_return_value(): 
 number1 = 1
 number2 = 2
 return(number1 + number2)
 
returned_value = add_two_numbers_and_return_value()
print (returned_value) 

def convert_temp(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32 
    kelvin = centigrade + 273.15
    return(fahrenheit, kelvin)
centigrade = 30

fahrenheit, kelvin = convert_temp(centigrade)
returned_value = convert_temp(centigrade)
print (returned_value)


def convert_temp(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32 
    kelvin = centigrade + 273.15
    return(fahrenheit, kelvin)
centigrade = 30

fahrenheit, kelvin = convert_temp(centigrade)
returned_value = convert_temp(centigrade)
print (returned_value)

def convert_temp2():
    centigrade = float(input("What value in celsius do you want to convert to fahrenheit and kelvin? "))
    fahrenheit = centigrade * 9.0 / 5.0 + 32 
    kelvin = centigrade + 273.15
    print("Converting celsius into fahrenheit and kelvin:")
    print("That's {} in fahrenheit and {} in kelvin.".format(fahrenheit, kelvin))
    return(fahrenheit, kelvin)
    
fahrenheit, kelvin = convert_temp2()
