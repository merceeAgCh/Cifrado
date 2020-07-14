# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:03:01 2020

@author: MAC
"""
import random


n1 = ['0','1','2','3','4','5','6','7','8','9']
n2= ['a','b','c','d','e','f','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#n2 = map(chr, range(97, 123))
n2.extend(n1)
normal = n2
f = open("alfabetoNormal.txt", "w")  
f.write(" ".join(normal))
f.close() 

random.shuffle(n2)
nuevo = n2
print("El nuevo alfabeto de cifrado es:")
print(nuevo)

f = open("alfabetoCifrado.txt", "w")  
f.write(" ".join(nuevo))
f.close()   


