# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:35:01 2018

@author: Kate Sorotos
"""

"""Operations, Strings and Variables"""

##############################################################################################
### Task 1 - simple operations
5-6
8*9
6/2
5/2
5.0/2
5%2
2*(10+3)
2*4

print(5-6)
print(8*9)
print(6/2)
print(5/2)
print(5%2)
print(2*(10+3))
print(2*4)

A=5-6
B=8*9
C=6/2
D=5/2
E=5.0/2
F=2*(10+3)
G=2*4

##############################################################################################
### Taks 2 - practicing with varaibles
age=5
age="almost three"
age=29.5
age='i really don\'t know!'
print(age)

##############################################################################################
### Task 3 - basic string manipulation 
print('hello'+'world')
print(("Joke \n") *3)
print("Chen " + str(3))
print("hello".upper())
print("GOODBYE".lower())
print('\n')
print("the lord of the rings".title())
print(("I will not be late \n") *10)

print(type(age))

s1='hello'+'world'
s2="joke " *3
s3=5

print(s1)
print(s2)
print(s3)

print(s1+s2*10)
print(s1+s2+str(s3))

result=(s1+s2+str(s3))
print(result)

strExample='a,b,c,d,e'
print(strExample)
SplitStr=strExample.split(',')
print(SplitStr)

##############################################################################################
### Task 4 - string formatting
age=5
like="painting"

age=6
age_description="My age is {} and I like {}.".format(age,like)
print(age_description)

age_description2="My age is {0} and I like {1}.".format(age,like)
print(age_description2)

#age=6
#print(age_description)

"""hobby=football 
basketball swimming
tennis"""

##############################################################################################
### Homework

print(10/3)
print(10%3)

a=1
a=a+1
print(a)
b='hello'
print(b)
c=b.title()
print(b)
print(c)
d='hello'
e=d.title()
print(d)
print(e)
name='Kate'
print(name)
f="Hello {0}!".format(name)
print(f)
name=('Kate ' + 'Sorotos')
f="Hello, {0}! ".format(name)
print(f)
print(f*5)

test = 'hello'
print(test + "\n") #print new line
print() #another way of printing a new line
print('\n') #print two new lines
