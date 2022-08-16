# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 01:03:08 2022

@author: 1993b
"""

kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

manzil = f"{kocha} ko\'chasi, {mahalla} mahallasi, {tuman} tumani {viloyat} viloyati."
print(manzil)

kocha = input("ko'changizni kiriting\n>>>")
mahalla = input("mahaallangizni kiriting\n>>>")
tuman = input("tumaningizni kiriting\>>>")
viloyat = input("viloyatingizni kiriting\n>>>")

manzil = f"{kocha} ko\'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati."
print("foydalanuvchi manzili\n>>>", manzil)
print("foydalanuvchi manzili\n>>>", manzil.title())
print("foydalanuvchi manzili\n>>>", manzil.capitalize())
print("foydalanuvchi manzili\n>>>", manzil.upper())
print("foydalanuvchi manzili\n>>>", manzil.lower())
