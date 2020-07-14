# -*- coding: utf-8 -*-
"""
@author: MAC
"""
from collections import Counter

f=open ('textoCifrado.txt','r')
contar= f.read()
f.close()

con=Counter(contar)
print(con)

f = open("Contar.txt", "w")
f.write("".join(con))
f.close()
