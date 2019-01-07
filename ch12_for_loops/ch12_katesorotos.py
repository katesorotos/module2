# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:27:01 2018

@author: Kate Sorotos
"""
"""The 'For' Loop"""

##############################################################################################
### Task 1 - loop through a list using for loop
my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]

for item in my_shopping_cart:
    print(item)
    
#for x in name_of_thing_to_iterate_through:
#    print(x)
    
##############################################################################################
### Task 2 - update list values

values = [875, 23, 451]

for val in values:
    print('----> ' + str(val))
    
print()

values = [875, 23, 451]

for val in values:
    print('----> ' + str(val+50))
    
print()

##############################################################################################
### Task 3 - create your own list
    
values = ['this', 55, 'that']

for item in values:
    print('***', item)

##############################################################################################
### Task 4 - loop through a string type
for char in "Yes":
    print(char)

print()

for word in "hello, my name is kate".split():
    print(word)
  
print()

##############################################################################################
### Task 5 - loop through a tuple

shopping_list = ('apples', 'bananas', 'grapes', 'oranges')
for item in shopping_list:
    print(item)
    
##############################################################################################
### Task 6 & 7 - loop through a dictionary 
    
densities = {'iron': (3, 94, 665), 'gold': (5, 30, 67), 'zinc': (9, 39, 5.4), 'lead': (114, 80, 83)}

#checking the keys of the dictionary
#casting to a list
metals = list(densities.keys())
print(metals)

#sorting the dictionary by their values, in reverse order
metals.sort(reverse = True, key = lambda m:densities[m])
print(metals)

key_value = sorted(densities.items(), key = lambda kv:kv[1][1], reverse = True)

for k, v in sorted(densities.items(), key = lambda kv:kv[1][1]):
    print(k, v[1])

#nested example
for metal, metal_value in key_value:
    print('metal: ', metal, '\n' 'price: ' , metal_value[1])

for metal in metals:
    print('{} = {}'.format(metal,densities[metal][0]))
    
    
for metal in metals:
    print(metal, densities[metal][1])
    
#formatting print fucntion
for metal in metals:
    if densities[metal][0]>8:
        print('{0:>8} = {1:5.1f}'.format(metal,densities[metal][0]))
print()

##############################################################################################
### Task 8 - combine loop and conditionals to filter values

#filtered  by density [0] 
#for metals with a density > 8 

#lead 114
#zinc 9

for metal in metals:
    if densities[metal][0]>8:
        print(metal, densities[metal][0])
    else:
       print(metal)
       
print()
##############################################################################################
### Task 9 - design a sum function 
        
values = [3, 12, 9]
total = 0 
for val in values:
    print('before adding ', val, 'total is ', total)
    total += val
    print('after adding ', val, 'total is ', total)
print('TOTAL: ' + str(total)) 

print()

def sumValues(l):
    sumV = 0
    for item in l:
        sumV += item
    return sumV
print(sumValues(values))

##############################################################################################
### Task 10 - using a loop with index values

values = [3, 12, 9]
for i in range (len(values)):
    values[i] = values[i] * 2
print(values)


wish_list = {'Puppies': (10, 150), 'TV\'s': (1, 2000), 'Chocolates': (20, 30), 'Kittens': (3, 300)}

#looping through a dict that prints both key and values
# gift = key
# item = value
for gift, item in wish_list.items():
    if wish_list[gift][0]>3:
        print('Yay! I got', item[1], gift)
    else:
        print('No! I want more', gift)
    
for i in range(3,10,4): #start at 3, stop at 10, step by 2
    print(i)
    
for i in range(10, 0, -2):
    print(i)
    
result = 0
n = 5
for i in range(1, n + 1):
    result += i
print(result)

values = [3, 12, 9, 11, 15, 8]

print()
for index in range(len(values)):
    print(index)

#start at 0, length, step 2
for index in range (0, len(values), 2):
    print(values[index])
     
##############################################################################################
### Task 11 - using a loop with the range function 
    
#class_mates = ['pam', 'muna', 'gracy', 'leanne', 'amina']
#for index in range(0, len(class_mates)):
#    if index == 'pam':
#        print('found her!,' class_mates[index])
#    else:
#        break
 
##############################################################################################
### Task 12 - using break in for loops     

numbers = [1,5,30,200,101,100,22]

for num in numbers:
    if num > 100:
        print('found it', num)
        break 

for index in range(len(numbers)):
    if numbers[index] > 100:
        print('Break:', numbers[index], 'with index', index)
        break 

print()
##############################################################################################
### Task 14 - using nested loops      

#keys must be unique
outer_vals_list = [1,2,3]
inner_vals_list = ['A', 'B', 'C']

outer_inner = {}
for oval in outer_vals_list:
    print(oval)
    for ival in inner_vals_list:
        print(ival)
        outer_inner[oval] = ival #assigning values to dict
        
        print(outer_inner)   
    
##############################################################################################
### Task 15 - using counters
        
colours = ['pink', 'pink', 'orange', 'green', 'pink', 'green', 'yellow', 'yellow']
colours_dict = {}

for item in colours:
    
    if item not in colours_dict:
        colours_dict[item] = 1
    else:
        colours_dict[item] = colours_dict[item] + 1
        print(colours_dict)
print()
##############################################################################################
### Task 14 - multiplication table with a for loop

for i in range (1,11):
    for j in range(1,11):
        print('{0:>3}'.format(i*j), end = '')
    print('\n')