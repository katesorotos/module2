# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:05:45 2018

@author: Kate Sorotos
"""

# dice game 1
#import random
#min = 1
#max = 6
#
#roll_again = "yes"
#
#while roll_again == "yes" or roll_again == "y" or roll_again == "Yes":
#    print("Rolling the dices...")
#    print("The values are....")
#    print(random.randint(min, max))
#    print(random.randint(min, max))

#    roll_again = input("Roll the dices again? ")
    

# dice game 2
import random
min = 1
max = 6
import time

name = input("What is your name? ")

def dice():
        player = input("Enter a number between 1 and 6: ")
        print("You rolled " + str(player) )

        computer = str(random.randint(min, max))
        print("The computer rolls..." )
        time.sleep(2)
        print("The computer has rolled a " + str(computer) )
  
        if computer == player :
            print("It's a draw",name.title()+"!")
        if player > computer :
            print("You won",name.title()+"!")
        if player < computer :
            print("Bad luck! You lost",name.title()+"!")

dice()


