# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:20:19 2021

@author: Pritesh
"""

KM = float(input("Enter value in Kilometer :"))

cov_fac = 0.621371

miles = KM*cov_fac

print("%0.2f kilometers is equal to %0.2f miles"%(KM,miles))