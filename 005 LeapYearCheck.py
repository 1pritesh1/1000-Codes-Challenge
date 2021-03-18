# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:27:39 2021

@author: Pritesh
"""

year = int(input(" Enter any year in four digit :"))

if (year % 4 ) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print("its a leap year")
        else:
            print("its not a leap year")
    else:
        print("its a leap year")
else:
    print("its not a leap year")
        



