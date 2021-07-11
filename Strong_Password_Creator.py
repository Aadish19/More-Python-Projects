[]=i8uo# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:10:01 2021

@author: adish
"""

secure_password = (('A','/|'),('a','@'),('d','9'),('i','|'),('s','$'),('h','|-|'))
def password_secure(password):
    for a,b in secure_password:
        password = password.replace(a,b)
        
    return password 

user_input = input("Provide Your password : ")

print(f"Yur new passwor is {password_secure(password)}")

