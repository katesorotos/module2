# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:15:26 2018

@author: Kate Sorotos
"""
"""Debugging and Intro to Project Management"""

userInput = input('Please give a number ')
#result = userInput -2
print(type(userInput)) 

#userInput = input('Please give me a number ')
#def simpleOperation(userInput):
#        intInput = int(userInput)
#        result = intInput - 2
#        print(result)
#        return result
    
def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2
result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)