# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:31:34 2018

@author: Kate Sorotos
"""

from shape import *
from pylab import random as r

class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
    def goto(self, x, y):
        self.figure.goto(x, y)
    def moveTick(self):
#        x = self.x + self.dx
#        y = self.y + self.dy
#        goto(self, x, y)
        pass
    
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
class Circle(MovingShape):
    def __init___(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)
        
self.x(0,0)
self.y(0,0)
self.dx(10)
self.dy(10)
