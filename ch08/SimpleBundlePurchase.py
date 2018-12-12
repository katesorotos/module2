# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:52:48 2018

@author: Kate Sorotos
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        print('\nPassword OK')
        print('\nTo request your balance enter "1"')
        print('To purchase data enter "2"')
        print('To top up your account enter "3"')
        print('\nWhich transaction would you like?' )
        print()
        transactionType = int(input('Please enter your choice: '))
        if transactionType == 1:
            print('Your balance is: £{}'.format(balance))
            print('Would you like another service? ')
            print('Type "y" for yes or "n" for no')
            restart = input().lower()
            if restart == 'y':
                DataBundlePurchase(truePasscode, balance)
            else:
                print('Thanks, have a nice day!')
        elif transactionType == 2:
            dataAmount(truePasscode, balance)
        elif transactionType == 3:
            topUp(truePasscode, balance)
        else:
            print('Error: please make your choice by entering "1" or "2"')
    else: 
        print('Password incorrect, would you like to try again? ')
        retryPassword(truePasscode, balance)
        
def retryPassword(truePasscode, balance):
    print('Type "y" for yes or "n" for no')
    retry = input().lower()
    if retry == 'y':
        DataBundlePurchase(truePasscode, balance)
    else:
        print('Thanks, have a nice day!')
    
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True 
    else:
        return False
    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    
def checkNumber(balance):
    number_1 = input('Please enter your phone number to proceed: ')
    number_2 = input('Please re-enter your phone number: ')
    if number_1 == number_2:
       dataAmount(balance)
    else: 
        print('Numbers did not match' '\n' 'Transaction cancelled.')
    

def dataAmount(truePasscode, balance):
    max = 100.00
    print('The maximum amount you are able to top up by is £100')
    print('Your top-up amount must be a multiple of 5')
    print()
    print('You have £' + str(balance) + ' remaining in your balance. How much money would you like to top up by? ')
    data = int(input())
    new_balance = round(balance - data,2)
    
    if data > max:
        print('I\'m afraid you are only able to top up by £100 or less')
        print('Transaction cancelled')
    elif data > balance:
        print('You do not have enough money in your balance to proceed.')
        print('Transaction cancelled')
    elif data == int(data/5)*5:
        print('Thanks for your purchase. You now have £' + str(new_balance) + ' left in your account.')
        print('Would you like another service? ')
        print('Type "y" for yes or "n" for no')
        restart = input().lower()
        if restart == 'y':
            DataBundlePurchase(truePasscode, balance)
        else:
            print('Thanks, have a nice day!')
    else:
        print('Transaction type not recognised.')
    
def topUp(truePasscode, balance):
    print('\nYour current balance is £' + str(balance))
    amount = int(input('How much would you like to top-up by today? £ '))
    new_amount = balance + amount
    
    print('You have topped up your account by £' + str(amount) + '\nYour balance is now £' + str(new_amount)) 
    print('Would you like another service? ')
    print('Type "y" for yes or "n" for no')
    restart = input().lower()
    if restart == 'y':
        DataBundlePurchase(truePasscode, balance)
    else:
        print('Thanks, have a nice day!')
    
    