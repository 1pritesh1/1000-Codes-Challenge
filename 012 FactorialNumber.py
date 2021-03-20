# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:15:13 2021

@author: Pritesh
"""

# Find factorial

num = int(input("Enter any number :"))

fctNum = 1

if num < 0:
    print("negtive number")
elif num == 0:
    print("the factorial for 0 is 1")
else:
    for i in range(1,num+1):
        fctNum=fctNum*i
    print("The factorial for ",num,"is ",fctNum)

