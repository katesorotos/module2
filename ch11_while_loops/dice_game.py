# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:55:03 2018

@author: Kate Sorotos
"""

from random import randint

    
def dice():
    number = randint(1, 6)
    number_1 = randint(1, 6)
    result = number + number_1
    
#    print("Welcome to the odd or even game!")
#    print("The computer will roll 2 dice and add the values together. You must decide whether the sum of these values is ODD or EVEN. ")
#    print("Enter '1' for EVEN, '2' for ODD, '3' for QUIT")
    
    choice = 0
    
    while choice == 1:
        choice = int(input("Please enter your choice: "))
        if result % 2 == 0:
            print("The computer rolled a " + str(number) + " and a " + str(number_1) + " making a sum of " + str(result))
            print("You win!")
        else: 
            print("You lose!")
        
dice()
    
#    if choice == 1:
#        check_result()
#    elif choice ==2:
#        check_result()
#    else:
#        print("Thanks for playing!")
#
#def check_result():
#    while result % 2 == 0:
#        print("You win!") 
#    else:
#        print("You lose!")
        
