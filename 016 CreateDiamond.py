# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:45:10 2021

@author: Pritesh
"""

line = '*'
max_length = 10
while len(line) <= max_length:
    print(line)
    line += "*"
while len(line) > 0:
    print (len(line))
    print(line)
    line = line[:]
    print (len(line))