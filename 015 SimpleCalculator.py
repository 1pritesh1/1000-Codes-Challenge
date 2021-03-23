# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:25:21 2021

@author: Pritesh
"""

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("selection your operation")
print("1. Addition")
print("2. Subtract")
print("3. multiply")
print("4. division")



while True:
    choice = input("enter number for your selection :")
    
    if choice in ('1','2','3','4'):
        num1 = (float(input("Enter your first number: ")))
        num2 = (float(input("Enter your second number: ")))
        if choice == '1':
            print(add(num1,num2))
        elif choice == '2':
            print(subtract(num1,num2))
        elif choice == '3':
            print(multiply(num1,num2))
        elif choice == '4':
            print(divide(num1,num2))
        break
    else:
        print("invalid number")

