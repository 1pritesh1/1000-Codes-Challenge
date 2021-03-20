# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:14:36 2021

@author: Pritesh
"""
#Semi-perimeter
#s=(a+b+c)/2
#Area
#√(s(s-a)*(s-b)*(s-c))

a=float(input("Enter first side : "))
b=float(input("Enter first second : "))
c=float(input("Enter first third : "))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5

print('the area of the trinagle is %0.2f' %area)