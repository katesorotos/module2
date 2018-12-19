# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:28:41 2018

@author: Kate Sorotos
"""

"""Compound Data Types 
Lists and Tuples"""

##############################################################################################
### Task 1 - create a list

my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits]

print(x[0])
print(x[1])
print(x[2])
print(x[3])

print(x[3][0]) #my_favourite_fruits, 'apple'

print(x[-1])
print(x[-2])
print(x[-3])
print(x[-4])

##############################################################################################
### Task 2 - modify the list 

#delete an item 
x.remove(my_favourite_fruits)
print(x)
#Overwrite
x[1] = 'and'
print(x)
#Append/Add
x.append('again')
print(x)

y = x    
y = x.append('hello')
print(x)
print(y)
#y = None

y = x 
x.append('hello')
print(x)
print(y)
#y = x


#List operations
x = ['the', 'cat', 'sat']
y = ['on', 'the', 'mat']
z = x + y
print(z)

a = set(z)
print(a)

##############################################################################################
### Task 3 - slicing a list

x = ['this', 'and', 'that', 'once', 'again']
print(x)
print(x[1:4])
print(x[0:-2])
print(x[3:5])
print(x[0:2])
print(x[-1:-3]) #empty 
print(x[0:0]) #empty
print(x[-3:1]) #empty
print(x[-3]) #everything after position prints

##############################################################################################
### Task 4 - sorting a list

x = [7,11,3,9,2]
y = sorted(x)
print(y)
x.sort()
print(x)

x = ['d', 'c', 'k', 'y', 's']
y = sorted(x) #generates a new sorted list 
print(y)
x.sort() #changes the original 
print(x)

x = [7,11,3,9,2]
print(x)
print(sorted(x))
print(sorted(x, reverse=True))

print()

x = [7,11,3,9,2]
print(x)
x.sort()
print(x)
x.sort(reverse = True)
print(x)

#Generic sorted() function 
x = ['banana', 'kiwi', 'grape', 'orange', 'pear']
print(x)
y = sorted(x)
print('Now x =', x)
print('Now y =', y)

#Object method .sort()
x.sort()
y = x.sort()
print('Now x =', x)
print('Now y =', y)

x.sort(reverse=True)
y = x.sort(reverse=True)
print('Now x =', x)
print('Now y =', y)
if x == 7:
    print(True)
else: 
    print(False)

##############################################################################################
### Task 5 - using tuples
    
a = [0,1,2,3,4,5,6,7,8,9] #list
del a[-1] #deletes position -1 '9'
print(a)
a[3] = 50 #changes position 3 of list to '50'
print(a)
a.append('z') #adds 'z' to end
print(a)

b = (0,1,2,3,4,5,6,7,8,9) #tuple
#del b[-1] #TypeError tuples are immutable
#print(b)

list(b) #generates new 'copy' of b as a list 
c = list(b) 
print(type(b)) #tuple
print(type(c)) #list

b = c
print(type(b)) #list
print(type(c)) #list

##############################################################################################
### Task 6 - using lambda function to sort a list 

a = [50,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
c = [2,4,6,8,10,12,14,16,18]

my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['aa', 'hw', 'fy', 'lf', 'sb', 'ed']
z = ['uj', 'sx', 'uj', 'fg', 'ww', 'cf']
y = sorted(x) 

x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]
print(x2)
print(sorted(x2, key=lambda s:s[0]))
print(sorted(x2, key=lambda s:s[1]))
print(sorted(x2, key=lambda s:s[2]))
print(sorted(x2, key=lambda s:s[3]))
print(sorted(x2, key=lambda s:s[2][3]))

x = [1,2,3,4]
y = [3,4,10,3]
z = [20,10,30,40]

x2 = [('a', a, 3, z), ('c', b, 1, y), ('b', c, 5, x)]
