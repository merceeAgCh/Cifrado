# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 21:00:27 2020

@author: MAC
"""

import AcondicionarTexto as at

texto = at.acondicionar()   #Recuperamos la lista de palabras ya acondicionadas

f = open("alfabetoNormal.txt", "r")  #ABRIMOS EL ARCHIVO DE TEXTO para leerlo
normal = f.read()
f.close()

f = open("alfabetoCifrado.txt", "r")  #ABRIMOS EL ARCHIVO DE TEXTO para leerlo
clave = f.read()
f.close()                   #Cerramos la sesion de lectura del texto (no debe quedar abierta)
        
    #clave = texto.split(" ") 
textoCifrado = []

for palabra in texto:
    nuevaPalabra=""
    for letra in palabra:
        try:
            indice = normal.index(letra)
            nuevaPalabra = nuevaPalabra + clave[indice]
        except:
            print("")
    textoCifrado.append(nuevaPalabra)
    
print("Texto normal")
print(texto)
print("")
print("Texto cifrado")
print(textoCifrado)

f = open("textoCifrado.txt", "w")  
f.write(" ".join(textoCifrado))
f.close() 
        
        
        
        
