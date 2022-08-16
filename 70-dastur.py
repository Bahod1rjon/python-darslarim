# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 16:15:11 2022

@author: 1993b
"""
login = input ("Loginni kiriting: ")
if login.lower () == 'admin' :
    print("Xush kelibsiz Admin, foydalanuvchilar royhatini ko`rasizmi?  " )
else:
    print(f"Xush kelibsiz {login.title()}")