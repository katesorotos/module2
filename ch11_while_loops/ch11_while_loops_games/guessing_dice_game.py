# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:59:21 2018

@author: Kate Sorotos
"""

from random import randint

def guessing_dice():
    
    max_attempt = 4
    attempt = 0
    die_1 = randint(1,6)
    die_2 = randint(1,6)
    result = die_1 + die_2
    
    print()
    print("Welcome to the guessing game!")
    print("The aim of the game is to guess the sum of two die the computer will roll")
    print("You have 4 guesses to get it right")
    print("Can you guess the number? ")
    
    while attempt < max_attempt:  
        attempt += 1
        
        guess = int(input("Make a guess: "))
        if guess > result:
            print("No! Too high!")
        elif guess < result:
            print("No! Too low!")
        else:
            print("Congratualations! You guessed the number correctly!")
            break
        
guessing_dice()