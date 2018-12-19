# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:55:44 2018

@author: Kate Sorotos
"""

"""Dictionaries"""

##############################################################################################
### Task 1 - create a dictionary, assign and update values 

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

##############################################################################################
### Task 2 - create a dictionary, assign and update values 
 
tel = {'kate': 949 , 'henri': 537, 'mia': 325}
print(tel['kate'])
print(tel['henri'])
print(tel['mia'])

##############################################################################################
### Task 3 - Look up/update

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

##############################################################################################
### Task 4 - retrieveing keys and values from a dictionary 

#getting keys and values from a dict
#output is not a dictionary
print(tel.keys()) 
print(tel.values())
type(tel.keys()) #dict_keys
type(tel.values()) #dict_values

##############################################################################################
### Task 5 - convert keys and value to list data type

#cast into list 
tel_keys = list(tel.keys())
print(tel_keys)

##############################################################################################
### Task 6 - sorting key errors 

#more informative message for user
#use a varaible in order to change value you wish to look up
#tel['winston']
d = 'winston'
if d in tel:
    print(d, ':', tel[d])
else:
    print(d, 'not found!')
    
##############################################################################################
###Task 7 - sorting a dictionary using lambda function 
    
counts = {'a': 3, 'c': 1, 'b': 5}
labels = list(counts.keys())
labels.sort(key=lambda k:counts [k])

class_mates = {'Pam': (5, 6, 8), 'Muna': (5, 8, 3), 'Chen': (4, 8, 5), 'Amina': (2, 4, 2), 'Kate': (3,14, 9)}
info = list(class_mates.keys())


#puts info(keys) in ascending order of class_mates
#['Amina', 'Kate', 'Chen', 'Pam', 'Muna']
info.sort(key=lambda v:class_mates[v][0]) #key's values
print(sorted(class_mates.items(), key = lambda kv: kv[1]))  #key value pair
print(sorted(class_mates.items(), key=lambda kv:kv[1][1]))

abc = {1: ("Kate", "March", 14), 
       2: ("Pam", "May", 6), 
       3: ("Muna", "June", 5)}

abc_keys = list(abc.keys())
abc_keys.sort(key=lambda k:abc[k][0])
#'k' represents each key 'k:abc[k]' = each key within the dictionary

#sorting dictionary values in descending order
densities = {'iron': 7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
metals = list(densities.keys())
print(metals)
metals.sort(reverse=True, key = lambda m:densities[m])
print(metals)
print(sorted(densities.items(), key = lambda kv: kv[1], reverse = True))

#sorted by key in descneding order
metals_1 = sorted(densities.items(), key = lambda kv: kv[0], reverse = True)

##############################################################################################
#Task 8 - sorting dictionary using lambda function 
metals = {'iron': (7.8, 120, 983),'gold': (19.3, 35, 456), 'zinc': (7.13, 2.9, 200), 'lead': (11.4, 22, 87)}
print(metals)
#metals (keys) = {key: (v1(density), v2(share prices), v3(experiments))...}

#returning keys' values to the dictionary 
metals_1 = list(metals.keys()) #cast to list
print(metals_1)
print(type(metals_1))
metals_1.sort(key=lambda v:metals[v]) #puts 'metals_2' in ascending order of metals
print(metals_1) #prints ['zinc', 'iron', 'lead', 'gold']

#retruning both key and values "key value (kv) pairs"
#key in positon 0 
#value in position 1
print(sorted(metals.items(), key = lambda kv:kv [0])) #key
print(sorted(metals.items(), key = lambda kv:kv [1])) #value
print(sorted(metals.items(), key = lambda kv:kv [1][0]))
print(sorted(metals.items(), key = lambda kv:kv [1][1]))
print(sorted(metals.items(), key = lambda kv:kv [1][2]))
print()

#metals in descending order of key
print(sorted(metals.items(), key = lambda kv:kv [0], reverse = True))
print()
#metals in descending order of density (v1)
print(sorted(metals.items(), key = lambda kv:kv [1][0], reverse = True))
print()
#metals in descending order of share price (v2)
print(sorted(metals.items(), key = lambda kv:kv [1][1], reverse = True))
print()
#metals in descending order of experiments (v3)
print(sorted(metals.items(), key = lambda kv:kv [1][2], reverse = True))
print()

#returns the third most valueable (v2) in descending order
print(sorted(metals.items(), key = lambda kv:kv [1][2], reverse = True))[2]

sorted(metals, reverse = True, key = lambda m:metals[m][1])