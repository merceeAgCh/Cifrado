# -*- coding: utf-8 -*-
"""
@author: MAC
"""
from collections import Counter


def contarLetras(nombre1,nombre2):
    f=open (nombre1 + '.txt','r')
    contar= f.read()
    f.close()
    
    con=Counter(contar)
    
    llave = []
    valor = []
    
    
    for i in con:   #Iterar el counter
        #print(i,con[i])
        llave.append(i)     #Crear una lista con las llaves 
        valor.append(con[i])    #Crear una lista con los valores
    
    f = open(nombre2 + '.txt', "w") #Abro el documento
    
    while llave:        #Mientras que la lista de llave tenga algun elemento (no este vacia)
        m = max(valor)              #Maximo de la lista valor
        indice = valor.index (m)    #Busco su indice para despues sacar el valor de la lista llave
        l = llave[indice]           #Busco la llave correspondiente al valor
            
        f.write(str(l) + "-" + str(m) + "/")    #Escribo llave, valor y un "/" para identofocar cada par
        
        valor.remove(m) #Eliminar el valor más grande
        llave.remove(l) #Eliminar la llave correspondiente al valor más grande
    
    f.close()
