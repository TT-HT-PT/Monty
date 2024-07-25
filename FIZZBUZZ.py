#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:47:55 2024

@author: hsavjani
"""
while True:
    name = str(input("Please enter your name  "))        
    try:
        num = int(input("Please enter a number  "))
    except:
        print("Please use a numeric digit")  
        continue
    if num < 1:
        print("Please enter a valid number")
        continue
    break
            
if num % 3 == 0 and num % 5 == 0:
    print("It's a FIZZBUZZ")
elif num % 3 == 0:
    print("It's a FIZZ")
elif num % 5 == 0:
    print("It's a BUZZ")
else:
    print("Its neither")

