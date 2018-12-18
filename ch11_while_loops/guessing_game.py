# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:52:10 2018

@author: Kate Sorotos
"""

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
        max_attempts -= 1 
        player_guess = int(input("Make a guess: "))
        print("Attempts made: " + str(attempt))
        print("You have " + str(max_attempts) + " attempts left")
        print("Result: ")
        
        if player_guess < number:
            print("No - Too low!")
        elif player_guess > number:
            print("No - Too high!")
        else:
            print("well done! You guessed it!")
            break 
        
guess(3, 10)