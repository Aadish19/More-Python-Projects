#!/usr/bin/env python
# coding: utf-8

# In[18]:



secure_password = (('A','/|'),('a','@'),('d','9'),('i','|'),('s','$'),('h','|-|'))

def password_secure(password):
    for a,b in secure_password:
        password = password.replace(a,b)
        
    return password 

password = input("Provide Your password : ")

print(f"Yur new passwor is {password_secure(password)}")


# In[17]:


SECURE = (('A','/|'),('b','6'),('s','&'),('k','|<'),('a','@'),('O','0'),('D','|)'),('K','|<'))

def passwordsecure(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    
    return password

password = input("Please provide your password here: ")
decision = input("Do you need UPPER case letters to be present? (y/n)")

if decision == 'y':
    print(f"Your new password is {passwordsecure(password)}")
else:
    print(f"Your new password is {passwordsecure(password.lower())}")



# In[ ]:




