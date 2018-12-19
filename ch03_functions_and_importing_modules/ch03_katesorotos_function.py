# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:50:06 2018

@author: Kate Sorotos
"""
"""Functions and Importing modules"""

### Task 2 - write a fucntion

def hello_world():
    add2_2=2+2
    print("Hello World!")
    print (add2_2)
    
### Task 4 - adding two numbers with a return

def add_two_numbers_and_return_value(): 
    number1 = 1
    number2 = 2
    return(number1 + number2)
 
    returned_value = add_two_numbers_and_return_value()
    print (returned_value) 

### Task 5 - converting temperature
    
def convert_temp(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32 
    kelvin = centigrade + 273.15
    return(fahrenheit, kelvin)
    
def convert_temp2():
    centigrade = float(input("What value in celsius do you want to convert to fahrenheit and kelvin? "))
    fahrenheit = centigrade * 9.0 / 5.0 + 32 
    kelvin = centigrade + 273.15
    print("Converting celsius into fahrenheit and kelvin: ")
    print("That's {} in fahrenheit and {} in kelvin.".format(fahrenheit, kelvin))
    return(fahrenheit, kelvin)
    


 
    
    