# -*- coding: utf-8 -*-
"""

@author: DELL
"""
carrito_compras=["Tablet", "Smart Whatch"]
ver_carrito=input("¿Deceas ver tu carrito de compras=  (si/no):")
n_veces=0

while (ver_carrito=="si" and n_veces<7):
    print(carrito_compras)
    n_veces+=1
    print (n_veces)
print("fin del bucle while")


carrito_compras=[]
agregar_producto=input("¿Quieres agregar un producto a tu carrito? (si/no)")

while (agregar_producto=="si"):
    nuevo_producto=input("ingresa el producto: ")
    carrito_compras.append(nuevo_producto)
    agregar_producto=input("¿Quieres agregar un producto a tu carrito? (si/no)")
print (carrito_compras)