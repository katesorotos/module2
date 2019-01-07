# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:09:48 2018

@author: Kate Sorotos
"""

from shape import *

frame = Frame()

x = 0   
y = 0

s1 = Shape('square', 100)
s1.goto(200,100)

s2 = Shape('circle', 100)
s2.goto(200,100)

s3 = Shape('diamond', 100)
s3.goto(200,100)

for i in range(100):
    x = x + 5
    y = y + 5 
    s1.goto(x,y)


