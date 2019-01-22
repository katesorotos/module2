# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:39:33 2019

@author: Kate Sorotos
"""

"""Counting words"""


def read_stop_words(text_file):
    stops = []
    stop_words = open(text_file, 'r')
    for line in stop_words:
        word = line.strip()
        stops.append(word) 
#    print(stops)
    return stops

stops = read_stop_words('stopwords.txt')  

def printTop20(text_file):
    moby_dick = open(text_file, 'r')  # moby_dick = name of file and mode ('r' = read) 
    top_words = {} #  create an empty dictionary for top_words
    for line in moby_dick: # for every line in mobydick.txt
        moby_words = line.split() # moby_words = every line.split() (divides a string where spaces appear returning as a list)
        for word in moby_words: # for each word in moby_dick ('mobydick.txt')
            if word in top_words: # if word is in dictionary counts add 1 to count
                top_words[word] += 1
            else: # if word is not in dictionary (top_words) start count at 1
                top_words[word] = 1
                
    sorted_words = sorted(top_words.items(), key = lambda kv: kv[1], reverse = True) # sorted in reverse order of top_words
#    print(sorted_words[:20]) # prints top 20 sorted_words 
    return sorted_words
           
sorted_words = printTop20('mobypara.txt')
 
def count_words(text_file, stops):
    counts = {} # create an empty dictionary for counts 
    moby_dick = open(text_file, 'r') # moby_dick = name of file and mode ('r' = read) 
    for line in moby_dick: # for every line in mobydick.txt
        moby_words_list = line.split() # moby_words = every line.split() (divides a string where spaces appear returning as a list)
        for word in moby_words_list: # for each word in moby_dick ('mobydick.txt')
            if word not in stops: # if word not in stops list
                if word in counts: # if word (k) is in dictionary counts add 1 to count
                    counts[word] += 1
                else: # if word (k) is not in dictionary (counts) start count at 1
                    counts[word] = 1
#    print(counts) # prints dictionary of counts 
    sorted_words_no_stops = sorted(counts.items(), key = lambda kv: kv[1], reverse = True) 
    print(sorted_words_no_stops[:20])
    return counts # returns dictionary of counts

count_words('mobypara.txt', stops)






    

