# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:59:39 2020

@author: DELL
"""

edad_cliente=int(input('ingresa tu edad'))
tarjeta_credito=edad_cliente>=18 and edad_cliente<=78
print('Puedes tener tarjeta de credito: ', tarjeta_credito)

descuento=edad_cliente==20 or edad_cliente==30
print('Puedes obtener el desceunto:', descuento)

cadena=input('Ingresa una palabra:')
resultado=len(cadena)>5 or cadena[2]=='h'
print (resultado)