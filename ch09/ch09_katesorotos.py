# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:28:41 2018

@author: Kate Sorotos
"""

"""Compound Data Types 
Lists and Tuples"""


my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits]

#print(x[0])
#print(x[1])
#print(x[2])
#print(x[3])
#
#print(x[3][0])
#
#print(x[-1])
#print(x[-2])
#print(x[-3])
#print(x[-4])

#Delete
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



#Slicing
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

#Sorting Lists
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

#Tuples
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
