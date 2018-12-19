# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:15:26 2018

@author: Kate Sorotos
"""
"""Debugging and Intro to Project Management"""

##############################################################################################
### Task 1 - script debugging using "print" function 

userInput = input('Please give a number ')
result = userInput -2
print(type(userInput)) 

##############################################################################################
### Task 2 - using break points to debug your code
userInput = input('Please give me a number ')
def simpleOperation(userInput):
        intInput = int(userInput)
        result = intInput - 2
        print(result)
        return result
    
def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)

##############################################################################################
""" Debug mode 

1. The first button is for you to start running your code until the break point
2. The second button allows you to run your code line-by-line until the breakpoint
3. The third button is for stepping into the sections (class and functions) that you would like to dig into more 
4. The fourth button is for you to step out when you geel that the error is not related to the current section
5. The fifth button is for you to go to the next break point
6. The last button is for you to exit debugging mode and go back to normal coding mode """
