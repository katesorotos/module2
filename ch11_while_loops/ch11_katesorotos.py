# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:11:36 2018

@author: Kate Sorotos
"""

"""while loops"""

##############################################################################################
### Task 1 - repeated division
x = 33

while x >= 1:
        print(x, ':', end='') #end'' is a parameter that prints a space rather than a new line
        x = x/2

print(x)#exit the while loop (conditon no longer true)

##############################################################################################
### Task 2 - triangular numbers
def triangularNumber(n): 
    number = 0
    while n > 0:
        number = number + n
        n = n - 1
    print(number)
    return number

triangularNumber(3)

##############################################################################################
### Task 2 - factorial numbers
def factorialNumber():
    n = int(input("Please enter a number: "))
    factorial = 1
    while n > 0:
        factorial = factorial * n 
        n = n - 1
    print(factorial)
    return factorial  

factorialNumber()

##############################################################################################
### Task 3 - studnet's marks
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

##############################################################################################
### Task 3 - student's marks  
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

##############################################################################################
###Task 4 - using break in while loops to exit

i = 55
while i > 10:
        print(i)
        i = i * 0.8
        if i == 35.2:
            break #ends the normal flow of the loop 
            
while True:
    askName = input("Please enter your name: ")
    if askName == 'done':
        
        break
    
    print("Hi, " + askName.title())
    
###############################################################################################
### Task 5 & 6 - designing a guessing number game program
    
from random import randint

def guess(attempts, range):
    attempt = 0
    max_attempts = 3
    player_guess = 1
    number = randint(1, range)
    print()
    print('Welcome to the guessing game! \nYou have ' + str(attempts) + ' attempts to guess a number between 1 and ' + str(range))
    print("Can you guess my secret number? ")
    while attempt < max_attempts:
        attempt += 1
 
        player_guess = int(input("Make a guess: "))
        print("Attempts made: " + str(attempt))
        print()
        print("Result: ")
        
        
        if player_guess < number:
            print("No - Too low!")

        elif player_guess > number:
            print("No - Too high!")

        else:
            print("well done! You guessed it!")
            break 
        
guess(3, 10)

    
    