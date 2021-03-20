# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 21:20:59 2021

@author: Pritesh
"""
num = int(input("Enter any number :"))

sum=0

temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + (digit **3)
    temp = temp // 10

if num == sum:
    print(num, "is armstrong number")
else:
    print(num,"is not armstring number")
    