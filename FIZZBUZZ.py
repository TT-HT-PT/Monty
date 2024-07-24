#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:47:55 2024

@author: hsavjani
"""

import math
while True:
    try:
        name = input("Please enter your name  ")
        num = int(input("Please enter a number  "))
        if num < 0:
            raise Exception("Please enter a valid number")
    finally:
        if num % 3 == 0 and num % 5 == 0:
            print("It's a FIZZBUZZ")
        elif num % 3 == 0:
            print("It's a FIZZ")
        elif num % 5 == 0:
            print("It's a BUZZ")
        else:
            print("Its neither")
