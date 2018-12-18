# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:11:36 2018

@author: Kate Sorotos
"""

"""while loops"""
#
##repeated division
#x = 33
#
#while x >= 1:
#        print(x, ':', end='') #end'' is a parameter that prints a space rather than a new line
#        x = x/2
#
#print(x)#exit the while loop (conditon no longer true)
#
##triangular number
#def triangularNumber(n): 
#    number = 0
#    while n > 0:
#        number = number + n
#        n = n - 1
#    print(number)
#    return number
#
#triangularNumber(3)
#
##factorial number
#def factorialNumber():
#    n = int(input("Please enter a number: "))
#    factorial = 1
#    while n > 0:
#        factorial = factorial * n 
#        n = n - 1
#    print(factorial)
#    return factorial  
#
#factorialNumber()
#
#grading student marks
def gradingStudentMarks():
    mark = 1
    while mark > 0:
        mark = int(input("Please enter your mark: "))  #user input must be inside while loop otherwise condition is forever true 
        if mark >= 70:
            print("Congratualtions! You got a first class mark.")
            
        elif mark >= 40:
            print("Well done! You passed.")
            
        else: 
            print("Fail.")
            
gradingStudentMarks()

#
didYouPass = 'yes'
while didYouPass == 'yes':
    mark = int(input("Please enter your mark: "))
    if mark >= 90:
            print("Congratualtions! You got an A*.")
    elif mark >= 70:
            print("Well done! You got a A.")  
    elif mark >= 60:
            print("You got a B.")   
    elif mark >= 50:
            print("You got a C.") 
    elif mark >= 40:
            print("You got a D.") 
    else: 
            print("I'm afraid you did not pass.")
            
    didYouPass = input("Did you pass? ")
#    
##early exit in while loops
#i = 55
#while i > 10:
#        print(i)
#        i = i * 0.8
#        if i == 35.2:
#            break #ends the normal flow of the loop 
            
#break statement
while True:
    askName = input("Please enter your name: ")
    if askName == 'done':
        
        break
    
    print("Hi, " + askName.title())
    
    