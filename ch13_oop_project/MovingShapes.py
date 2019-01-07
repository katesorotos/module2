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
        
#        self.x = 0
#        self.y = 0
        
### creating random movement in x
        self.dx = 5 + 10 * r()     
### move in positive and negative directions
        if r() < 0.5:
            self.dx = 5 + 10 * r()
        else:
            self.dx = -5 + -10 * r()
            
### creating random movement in y
        self.dy = 5 + 10 * r() 
### move in positive and negative directions
        if r() < 0.5:
            self.dy = 5 + 10 * r()
        else:
            self.dy = -5 + -10 * r()
                
#        self.goto(self.x, self.y)
        
        
### minimum and maximum start position of x and y
        def min_max_start(self, diameter):
            diameter_2 = diameter / 2
        
            self.minx = diameter / 2
            self.maxx = frame.width - (diameter_2)
        
            self.miny = diameter / 2
            self.maxy = frame.height - (diameter_2)
        min_max_start(self, diameter)
              
### adding random variation for the start positions
        self.x = self.minx + r () * (self.maxx - self.minx)
        self.y = self.miny + r () * (self.maxy - self.miny)
        
    def goto(self, x, y):
        self.figure.goto(x, y)
        
    def moveTick(self):

### hitting the wall
        if self.x <= self.minx or self.x >= self.maxx:
            self.dx = (self.dx) * -1
        if self.y <= self.miny or self.y >= self.maxy:
            self.dy =- self.dy
            
            
        self.x += self.dx
        self.y += self.dy
        self.figure.goto(self.x, self.y)
    
### squares vs diamonds vs circles
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)
        
        
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
        def min_max_start(self, diameter):
            diameter_2 = diameter * 2
            
            self.minx = diameter / 2
            self.maxx = frame.width - (diameter_2)
        
            self.miny = diameter / 2
            self.maxy = frame.height - (diameter_2)
        min_max_start(self, diameter)
        
class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)  
        
        
        
        
