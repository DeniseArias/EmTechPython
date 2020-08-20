# -*- coding: utf-8 -*-
"""

@author: DELL
"""
mi_cadena="Hola mundo"
mi_cadena2='Hola mundo!'
print(mi_cadena)

cadena_con_comillas ='Javier dijo: "Hola mundo"'
print(cadena_con_comillas)

comillas_simples ="hello, it's me!"
print(comillas_simples)

#usado en python para eliminar el sentido de los caracteres
cadena_con_comillas ="Javier dijo: \"Hola mundo!\""
print(cadena_con_comillas)

multilinea="""hola bienvenido,

actualmente estas en el curso de python
"""
print(multilinea)

nombre=" Javier "
saludo="Buenos dias"
union_cadenas= saludo+nombre
print (union_cadenas)

edad=23
numero_como_cadena=str(edad)
print("Tu edad es "+numero_como_cadena)