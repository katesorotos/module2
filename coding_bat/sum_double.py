# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:44:04 2018

@author: Kate Sorotos
"""

#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#
#
#sum_double(1, 2) → 3
#sum_double(3, 2) → 5
#sum_double(2, 2) → 8

def sum_double(a, b):
  if a == b:
    return (a+b) * 2
  else:
    return a+b
