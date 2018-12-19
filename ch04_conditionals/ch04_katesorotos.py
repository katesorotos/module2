
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:59:09 2018

@author: Kate Sorotos
"""

"""Conditionals"""

##############################################################################################
### Task 1 - logic operators
print("this" == 'this')
print(3 >= 4)
print(3 >= 2)
print(5!=3)
print(5!='some string')


age = 15 
isaTeen = age >= 13 and age <= 19
print(isaTeen)

age = 22
isaTeen = age >= 13 and age <= 19
print(isaTeen)

if age >= 13 and age <= 19:
    print(True)
else: 
    print(False)
    
if 5>=10:
    print(True)
else:
    print(False)

##############################################################################################
### Task 3 - using if statements
number = input("Enter a number between 1 and 10: ")
number = int(number)

if number>10:
    print("Too high!")
if number<=0:
    print("Too low!")
if 0 < number <= 10:
    print("Don't know!")

##############################################################################################   
### Task 4 - using else statments
 
if number>10:
    print("Too high!")
if number<=0:
    print("Too low!")
else:
    print("Don't know!")

#first else statement practice 
#final else will only catch above if statment
    
##############################################################################################    
### Taks 5 - using elif statements 
#order is important!

age = 15

if age < 13:
    print('child')
elif age < 18:
    print('teen')
elif age < 65:
    print('adult')
else: 
    print('pensioner')
    
def checkTeen2(age):
    if age >=13 and age <=19:
        print("They are a teen!")
    else:
        print("Not a teen!")