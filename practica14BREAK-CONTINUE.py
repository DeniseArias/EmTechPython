# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:18:40 2020

@author: DELL
"""

autos=["correcto","correcto","correcto","defectuoso","correcto","defectuoso","correcto",]

for estado in autos:
    if (estado == "defectuoso"):
        print("Auto defectuoso,enviado a revisión")
        continue
    print("Este auto está: " + estado)
    print("Enviado para distribución")

for caracter in "Python":

  if caracter == "h":

    continue

    print ( "Esta es una h" )

  print ( caracter )