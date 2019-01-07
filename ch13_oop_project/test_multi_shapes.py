# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:03:22 2018

@author: Kate Sorotos
"""

from MovingShapes import *
frame = Frame()
numshapes = 3
shapes = []
size = 60
for i in range(numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Diamond(frame,size))
    shapes.append(Circle(frame,size))

for i in range(300):
    for shape in shapes:
        shape.moveTick()
        
frame.close()
        

        

        