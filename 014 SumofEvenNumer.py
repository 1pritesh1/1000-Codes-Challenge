# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:15:24 2021

@author: Pritesh
"""

MaxNum = int(input("enter any number:"))
sum = 0

for num in range(0,MaxNum+1):
    if (num%2 == 0):
        print(num)
        sum=sum+num
print("the sum of even numbers from 1 to ",MaxNum," is ",sum)