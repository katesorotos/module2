# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:42:49 2018

@author: Kate Sorotos
"""

from MovingShapes import *

frame = Frame(300, 300)
shape1 = Square (frame, 100)
x = 0 
y = 0


for i in range(100):
    shape1.moveTick()
    

