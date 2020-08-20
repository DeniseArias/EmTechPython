# -*- coding: utf-8 -*-
"""

@author: DELL
"""

productos_descuento=['Computadora','Televisión', 'Teclado', 'Mouse', 'Cartera', 'Monitor']
sin_stock=['Camara','Celular', 'Reloj','Memoria']


producto=input('Ingresa un producto: ')

if(producto in productos_descuento):
    print('este producto si esta en descuento')
    print('!Aprobecha la oferta¡')
elif (producto in sin_stock):
    print('Lo sentimos el producto se encuentra agotado')
else:
    print('Lo sentimos este producto no esta en oferta')
    
    
print('fin if')