# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fib(n):
    i, num1, num2 = 0, 1, 1
    result = []
    while i < n:
        result.append(num1)
        num1, num2 = num2, num1 + num2 
        i = i + 1
    print('[', result, ']')
    
fib(4)