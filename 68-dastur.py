# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:26:28 2022

@author: 1993b
"""

suhbatdoshlar = []
print("Bugun nechta odam bilan suhbatlashdingiz?\n>>>")
a = int(input())
for n in range(a):
    suhbatdoshlar.append(input(f"{n+1} suhbatlashgan odamingizni ismi nima?  "))
print(suhbatdoshlar)