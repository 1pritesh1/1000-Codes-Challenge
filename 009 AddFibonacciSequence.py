# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:53:49 2021

@author: Pritesh
"""
nterms = int(input('Enter how many terms:'))

n1 = 0
n2 = 1

count=0

# chcek if nterm is valid
if nterms <=0:
    print(' enter positive number')
elif nterms==1:
    print('enter sequence upto',nterms)
    print(n1)
# later
else:

    while count < nterms:
        print(n1)
        fsq=n1+n2
        n1 = n2
        n2 = fsq
        count = count + 1
    
