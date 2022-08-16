# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 23:35:01 2022

@author: 1993b
"""

taomlar =['osh','manti','sho`rva', 'lagmon','chuchvara']
nonushta = taomlar[:]
nonushta.remove('manti')
nonushta.remove('lagmon')
nonushta.remove('chuchvara')
nonushta.append('non va choy')
nonushta.append('qaymoq')
nonushta.append('choy')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
print(nonushta)