# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:55:05 2018

@author: Kate Sorotos
"""

from random import randint


def dice():
    
    choice = 0
    
    print()
    print("Welcome to the odd or even game!")
    print("The computer will roll 2 dice and add the values together. You must decide whether the sum of these values is ODD or EVEN. ")
    print("Enter '1' for EVEN, '2' for ODD, '3' for QUIT")
#    choice = int(input("Please enter your choice: "))

    while choice != 3:
        number = randint(1, 6)
        number_1 = randint(1, 6)
        result = number + number_1      
        choice = int(input("Please enter your choice: "))
        
        if choice == 1 and result % 2 == 0:
            print("You guessed it would be EVEN")
            print("The computer rolled a " + str(number) + " and a " + str(number_1) + " making a sum of " + str(result))
            print("The result is EVEN")
            print("You win!")
        elif choice == 2 and result % 2 != 0:
            print("You guessed it would be ODD")
            print("The computer rolled a " + str(number) + " and a " + str(number_1) + " making a sum of " + str(result))
            print("The result is ODD")
            print("You win!")
        elif choice == 1 and result % 2 != 0:
            print("You guessed it would be EVEN")
            print("The computer rolled a " + str(number) + " and a " + str(number_1) + " making a sum of " + str(result))
            print("The result is ODD")
            print("You lose!")
        elif choice == 2 and result % 2 == 0:
            print("You guessed it would be ODD")
            print("The computer rolled a " + str(number) + " and a " + str(number_1) + " making a sum of " + str(result))
            print("The result is EVEN")
            print("You lose!")
    else:
        print("Thanks for playing!")

dice() 


    