# Escribe una función llamada contadorLetras. Esta fucnión recibe como parámetro
# un cadena de caracteres (string). La función retornará un diccionario con el número de veces
# que se encuentra cada letra dentro del string.

from os import lseek


def contadorLetras(caracteres):
    diccionario = {}
    for letra in caracteres:
        if letra in diccionario :
            diccionario[letra] += 1
            print(diccionario)
        else:
            diccionario[letra] = 1
        
    return diccionario
        
texto = "hola como estas, esto es un conteo de letras"
print(contadorLetras)