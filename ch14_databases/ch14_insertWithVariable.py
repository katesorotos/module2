# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:59:54 2019

@author: Kate Sorotos
"""

import sqlite3
import time
import datetime
import random 

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)', (unix, date, keyword, value))
    conn.commit()