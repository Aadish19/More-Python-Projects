# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 22:27:37 2021

@author: adish
"""
# Simple Exception Handling
#try:
#    open("contents.txt")
#except Exception:
#    print("Sorry For Inconvinience \n We Are Working On it")
    
    
# Developer Like Exception Handling
#try:
 #   open("contents.txt")
    
#except FileNotFoundError as g:
#    print(g)
#except Exception as e:
 #   print(e)

    
# Raising an Exception
try:
    open("corrupt.txt")
    if f.name == "corrupt.txt":
        raise Exception
except FileNotFoundError as g:
    print(g)
except Exception as e:
    print(e)
    
finally:
    print("Ye to hona hi hai")