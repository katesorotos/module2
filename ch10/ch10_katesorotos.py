# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:55:44 2018

@author: Kate Sorotos
"""

"""Dictionaries"""

#Syntax 
{'bo':50000, 'al':20000, '7':('Joke','Chen','Bond')}

salary = {}
salary['al'] = 20000
salary['al'] += 2000
print(salary)
salary['bo'] = 50000
salary['bo'] = 55000
print(salary)

{'a': 'Kate', 'b': 'Sorotos', 'c':23}
name = {}
name['a'] = 'Kate'
print(name)

#last three digits of tel no.
tel = {'kate': 949 , 'henri': 537, 'mia': 325}
print(tel['kate'])
print(tel['henri'])
print(tel['mia'])

#updating to last four digits of tel no.
#change to string data type if you want to just add one number
tel['kate'] = 5949
print(tel['kate'])
tel['henri'] = 4537
print(tel['henri'])
tel['mia'] = 6325
print(tel['mia'])

#deleting a key value
del tel['henri']
print(tel)

#getting keys and values from a dict
#output is not a dictionary
print(tel.keys()) 
print(tel.values())
type(tel.keys()) #dict_keys
type(tel.values()) #dict_values

#cast into list 
tel_keys = list(tel.keys())
print(tel_keys)

#avoiding key errors
#more informative message for user
#use a varaible in order to change value you wish to look up
#tel['winston']
d = 'winston'
if d in tel:
    print(d, ':', tel[d])
else:
    print(d, 'not found!')