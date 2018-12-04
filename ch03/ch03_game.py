# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:05:45 2018

@author: Kate Sorotos
"""

# dice game 1
import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y" or roll_again == "Yes":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = input("Roll the dices again? ")
    

# dice game 2
import random
import time

name = input("What is your name? ")

def dice():
        player = input("Enter a number between 1 and 6... ")
        print("You rolled " + str(player) )

        computer = str(random.randint(1, 6))
        print("The computer rolls...." )
        time.sleep(2)
        print("The computer has rolled a " + str(player) )
  
        if computer == player :
            print("It's a draw",name.title()+"!")
        elif player > computer :
            print("You won",name.title()+"!")
        elif player < computer :
            print("Bad luck! You lost",name.title()+"!")

dice()


##2. hangman    
#import time
#
#name = input("What is your name? ")
#print("Hello, " + name, "Time to play hangman!")
#print("")
#time.sleep(1)
#print("Start guessing...")
#time.sleep(0.5)
#
#word = "secret"
#guesses = ''
#turns = 10

#while turns > 0:         
#    failed = 0                 
#    for char in word:      
#        if char in guesses:    
#            print(char,)   
#        else:
#            print("_",)    
#            failed += 1    
#    if failed == 0:        
#        print("You won!")  

#        break       
       
#    print
#    guess = input("guess a letter:") 
#    guesses += guess                    
#    if guess not in word:  
#        turns -= 1        
#        print("Wrong")
#        print("You have", + turns, 'more guesses') 
#        if turns == 0:           
#            print("You Loose")