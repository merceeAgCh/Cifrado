# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:43:30 2020

@author: MAC
"""

def quitaAcentos(s):    #Funcion para quitar acentos
    replacements = (    #Reemplaza los acentos por letras sin acentos
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "nn"),     #CAMBIAR ñ por n
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.lower(), b.lower())
    return s

def quitaSignos(s):    #Funcion para quitar signos
    replacements = (    #Reemplaza los acentos por una cadena vacia
        ("¿", ""),
        ("?", ""),
        ("¡", ""),
        ("!", ""),
        ("$", ""),
        ("#", ""),
        ("%", ""),
        ("&", ""),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.lower(), b.lower())
    return s



def acondicionar():         #DEFINICION DEL MODULO
    nuevoTexto = []                 #Definimos una lista
    f = open("texto.txt", "r")  #ABRIMOS EL ARCHIVO DE TEXTO para leerlo
    texto = f.read()
    f.close()                   #Cerramos la sesion de lectura del texto (no debe quedar abierta)
        
    texto = texto.split(" ")        #Cortamos todo el texto en palabras dividiendo todo con espacios
    for w in texto:
        x = w.lower()               #Ponemos todo en minusculas
        y = quitaAcentos(x)         #Llamamos a la funcion que quita acentos
        z = quitaSignos(y)          #Llamamos a la funcion quitaSignos
        
        nuevoTexto.append(z)        #Llenamos la lista con las palabras ya acondiconadas
        
    return nuevoTexto



