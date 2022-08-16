# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 21:44:42 2022

@author: 1993b
"""

frends = []
frends.append("Ozod")
frends.append("Jamshid")
frends.append('Alisher')
frends.append("Jalil")
frends.append('Ali')
print(frends)
frends.remove("Jalil")
frends.remove("Ali")
print(frends)
frends.insert(2,"Murot")
frends.insert(0, "Xuja")
frends.append('Furqat')
print(frends)
mehmonlar = []
mehmonlar.append(frends.pop(2))
mehmonlar.append(frends.pop(4))
mehmonlar.append(frends.pop(0))
print("\nKelmagan mehmonlar:", mehmonlar)