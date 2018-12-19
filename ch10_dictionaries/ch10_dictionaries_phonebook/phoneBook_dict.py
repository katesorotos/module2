# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:15:47 2018

@author: Kate Sorotos
"""

"""phoneBook_dict"""



def addingPhonebookInfo(phonebook):
    
    name = input('What is your name? ')
    phone_number = input('What are the last three digits of your phone number? ')
    lucky_number = input('What is your lucky number? ')
    postcode = input('What is your postcode? ').lower()
    city = input('What city do you live in? ').lower()
    age = input('What is your age? ')

    phonebook[name.title()] = int(phone_number), int(lucky_number), postcode.upper(), city.title(), int(age
)    
    print()
    print('Updated phonebook with new information.')
    print('Phonebook: ')
    print(phonebook)
    print()
    print('Would you like to add another class mate\'s information? ')
    print('Type "y" for yes and "n" for no.')
    add_another = input().lower()

    if add_another == 'y':
       addingPhonebookInfo(phonebook)
       return phonebook
    else:
       print('Thanks for updating the phonebook today.')
       return phonebook
    
def sortAgain():
    print()
    print('Would you like to sort the phonebook in another way? ')
    print('Type "y" for yes and "n" for no.')
    sort_again = input().lower()
    
    if sort_again == 'y':
           sortingOptions()
    else:
        print('Thanks for updating the phonebook today.')
    
def sortbyName():
    sort_by_name = str(sorted(phonebook.items(), key = lambda kv:kv [0]))
    print('Phonebook sorted by name: \n' + sort_by_name)
    print()
    sortAgain()

def sortbyCity():
    sort_by_city = str(sorted(phonebook.items(), key = lambda kv:kv [1][3]))
    print('Phonebook sorted by city: \n' + sort_by_city)
    sortAgain()

def sortbyLuckyNumber():
    sort_by_lucky_number = str(sorted(phonebook.items(), key = lambda kv:kv [1][1]))
    print('Phonebook sorted by lucky number: \n' + sort_by_lucky_number)
    sortAgain()

def differencefromQueen():
    print('Please give the name of the classmate whose age you would like to compare with the Queen\'s age ')
    classmate = input().title()
#    list_of_names = list(sorted(phonebook))
    diff = 92 - phonebook[classmate][4]
    print('The difference in age between your classmate ' + classmate + ' and the Queen is: ' + str(diff) + ' years')
    print()
    sortAgain()
    
def sortingOptions():
    print('How would you like to sort the phonebook? ')
    print('1. by name')
    print('2. by city')
    print('3. by lucky number')
    print('4. compare classmate\'s age with the Queen\'s')
    sort_by = int(input('Please type either "1", "2" or "3" to proceed. '))
    if sort_by == 1:
        sortbyName()
        print()
    elif sort_by == 2:
        sortbyCity()
        print()
    elif sort_by == 3:
        print()
        sortbyLuckyNumber()
    elif sort_by == 4:
        print()
        differencefromQueen()
    else:
        print('Sorry that wasn\'t an option, please choose "1", "2" or "3"')
        

phonebook = {'Pam': (452, 5, 'NW5 3HG', 'London', 30), 
 'Kate': (949, 14, 'B14 7RT', 'Birmingham', 23), 
 'Amina': (324, 7, 'BS5 5LP', 'Bristol', 20),
 'Muna': (646, 9, 'CF7 8TR', 'Cardiff', 25)}

phonebook = addingPhonebookInfo(phonebook)
print()
sortingOptions()
        

f = open("phonebook.txt","w")
f.write( str(phonebook) )
f.close()
