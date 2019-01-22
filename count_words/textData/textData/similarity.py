# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:51:11 2019

@author: Kate Sorotos
"""
"""Document similarity task"""

### Reads stopwords and appends them to empty list
def read_stop_words(textfile):
    stops = []
    stop_words = open(textfile, 'r')
    for line in stop_words:
        word = line.strip()
        stops.append(word) 
#    print(stops)
    return stops

stops = read_stop_words('stopwords.txt') 

### Counts frequency words in george01.txt file appear and appends them to dictionary 
def george_1_count(textfile):
    george_1_words = {}
    george_1 = open(textfile, 'r')
    for line in george_1:
        george_words = line.split()
        for word in george_words:
            if word not in stops:
                if word in george_1_words:
                    george_1_words[word] += 1
                else:
                    george_1_words[word] = 1
#    print(george_1_words)
    return george_1_words

george_1_words = george_1_count('george01.txt') # saves returned dict to function 

print()

### Counts frequency words in george02.txt file appear and appends them to dictionary 
def george_2_count(textfile):
    george_2_words = {}
    george_2 = open(textfile, 'r')
    for line in george_2:
        george_2_words_split = line.split()
        for word in george_2_words_split:
            if word not in stops:
                if word in george_2_words:
                    george_2_words[word] += 1
                else:
                    george_2_words[word] = 1
#    print(george_2_words)
    return george_2_words

george_2_words = george_1_count('george02.txt') # saves returned dict to function 

### Removes duplicate words from dict 'george_1_words' into empty list
def remove_duplicate_george_1(george_1_words):
    george_1_remove_duplicate = []
    count_george_1 = 0
    for item in george_1_words:
        if item not in george_1_remove_duplicate:
            george_1_remove_duplicate.append(item)
            count_george_1 += 1
    print(count_george_1)
    print(george_1_remove_duplicate)
    return george_1_remove_duplicate

george_1_remove_duplicate = remove_duplicate_george_1(george_1_words)

### Removes duplicate words from dict 'george_2_words' into empty list
def remove_duplicate_george_2(george_2_words):
    george_2_remove_duplicate = []
    count_george_2 = 0
    for item in george_2_words:
        if item not in george_2_remove_duplicate:
            george_2_remove_duplicate.append(item)
            count_george_2 += 1
    print(count_george_2)
    print(george_2_remove_duplicate)
    return george_2_remove_duplicate

george_2_remove_duplicate = remove_duplicate_george_2(george_2_words)

### Counts words in common and appends them to empty list 'count_words_in_common'
def words_in_common(george_1_remove_duplicate, george_2_remove_duplicate):
    count_words_in_common = []
    count = 0
    for item in george_1_remove_duplicate:
        if item in george_2_remove_duplicate:
            count_words_in_common.append(item)
            count += 1
    print(count)
    print(count_words_in_common)
    return count

count = words_in_common(george_1_remove_duplicate, george_2_remove_duplicate)

### Generates similarity score
#def similarity_calculated(george_1_remove_duplicate, george_2_remove_duplicate, count):
#    
#    unique_words_1 = int(george_1_remove_duplicate[1])
#    unique_words_2 = int(george_2_remove_duplicate[1])
#    
#    overlap = count/ (unique_words_1 + unique_words_2)
#    overlap_percent = overlap * 100
#    
##    overlap = count / int((george_1_remove_duplicate) + int(george_2_remove_duplicate))
#    print(overlap)
#    print(overlap_percent)
#    
#similarity_calculated(george_1_remove_duplicate, george_2_remove_duplicate, count)
