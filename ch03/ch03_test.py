# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:45:33 2018

@author: Kate Sorotos
"""

from ch03_function import *

#converting temp to fahrenheit and kelvin
centigrade = 30
print(convert_temp(centigrade))

#converting temp to fahrenheit and kelvin with user input
fahrenheit, kelvin = convert_temp2()
print(convert_temp2())

print()

#returning the value of two numbers added together
returned_value = add_two_numbers_and_return_value()
print(returned_value) 

#dice game
dice()