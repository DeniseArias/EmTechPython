# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:08:57 2020

@author: DELL
"""
import Users as u
import lifestore_file as lf
from datetime import datetime as dt #Utilizaremos para obtener el año actual



user=""
contrasenia=""
opc=1
error_seleccion=1
error_usuario=0
while user!="0" and contrasenia!="0":
    print("")
    print ("------------------------------------------------------------------------------------------------")
    print("Bienvenido a su sistema de análisis de ventas")
    print("Por favor ingrese su usuario y contraseña \n O si decea salir ingrese unicamente 0 en el usuario y contraseña")
    user = input("Ususario: ")
    contrasenia = input("Contraseña: ")
    """
        Creador: Denise Etaira Arias González
        Función: Inicia la autenticación, para esto buscara un usuario y contraseña ingresados, de no encontrar
                 lanzara el error de la linea 777
    """
    for usuario in u.usuarios:
        if (user == usuario[0] and contrasenia == usuario[1]):
            error_usuario=0
            print("")
            print ("------------------------------------------------------------------------------------------------")
            print("Bienvenido/a " + usuario[0]+" " + "Usted tiene permisos de "+ usuario[2])
            error_seleccion=1
            opc=1
            while(opc!=0):
                print("")
                #Mostramos menú segun el tipo de usuario predefinido en la lista de usuarios
                print("Estas son las opciones que tienes disponibles")
                if(usuario[2]=="ADMINISTRADOR"):
                    while(error_seleccion==1):
                        error_seleccion=0
                        print ("0) Salir del sistema")
                        print ("1) Top 20 de productos con mayores ventas y Top 20 con menores ventas")
                        print ("2) Top 20 de productos con mayores busquedas y Top 20 con menores busquedas")
                        print ("3) Top 20 de productos con mayores reseñas")
                        print ("4) Top 20 de productos con peores reseñas promedio (no devueltos)")
                        print ("5) Top 20 de productos con peores reseñas promedio (si devueltos)")
                        print ("6) Total de ingresos y las ventas promedio mensuales")
                        print ("7) Total anual y meses con mas ventas")
                        opc=input("Ingresa la opción que deceas consultar: ")
                        """
                            Creador: Denise Etaira Arias González
                            Función: Verificamos que lo ingresado por el usuario sea un número, para posteriormente
                                     verficiar si la opción seleccionada existe, de caer en cualquiera de los dos errores
                                     mencionados anteriormente, se desplegara el error de la linea 68
                        """
                        try:
                            opc = int(opc)
                            if (opc>=8 or opc<0):
                                error_seleccion=1
                            else:
                                error_seleccion=0
                        except ValueError:
                            error_seleccion=1
                        if(error_seleccion==1):
                            print ("------------------------------------------------------------------------------------------------")
                            print("La opción seleccionada no es valida \nPor favor ingrese un número del 0 al 7 para indicar la opcion que desea consultar")
                            print ("------------------------------------------------------------------------------------------------")
                elif(usuario[2]=="USUARIO"):
                    while(error_seleccion==1):
                        error_seleccion=0
                        print ("0) Salir del sistema")
                        print ("1) Top 20 de productos con mayores ventas")
                        print ("2) Top 20 de productos con mayores busquedas")
                        print ("3) Top 20 de productos con mejores reseñas promedio")
                        print ("4) Top 20 de productos con peores reseñas promedio (no devueltos)")
                        print ("5) Top 20 de productos con peores reseñas promedio (si devueltos)")
                        opc=input("Ingresa la opción que deceas consultar: ")
                        try:
                            opc = int(opc)
                            if (opc>=6 or opc<0):
                                error_seleccion=1
                            else:
                                error_seleccion=0
                        except ValueError:
                            error_seleccion=1
                        if(error_seleccion==1):
                            print ("------------------------------------------------------------------------------------------------")
                            print("La opción seleccionada no es valida \nPor favor ingrese un número del 0 al 5 para indicar la opcion que desea consultar")
                            print ("------------------------------------------------------------------------------------------------") 
                else:
                    print ("------------------------------------------------------------------------------------------------")
                    print("Al parecer no se cuenta con un rol valido para el sistema \nPor favor contacta con el área de sistemas")
                    print ("------------------------------------------------------------------------------------------------")
                    break
                #Terminan validaciones de seleccion de opción
                
                
                if(opc==1):
                    print("Usted selecciono: ")
                    print ("1) Top 20 de productos con mayores ventas y Top 20 con menores ventas")
                    
                    ventas_agrupadas=[]
                    ventas_categorias=[]
                    contador=1
                    
                    """
                        Creador: Denise Etaira Arias González
                        Función: Creamos una lista con el id del producto y creamos una sumatoria para 
                                obtener el numero de incidencias existentes
                    """            
                    for venta in lf.lifestore_sales:
                        grupo_encontrado=0
                        for grupo in ventas_agrupadas:
                            if (venta[1]== grupo[0]):
                                grupo[1]+=1
                                grupo_encontrado=1
                                break
                        if(grupo_encontrado==0):
                            ventas_agrupadas.append([venta[1],1])
                            
                    """
                        Creador: Denise Etaira Arias González
                        Función: Con la lista anterior creamos una mas especializada que contendra      
                                Toda la informacion necesaria para la impresión correcta segun se necesite
                    """
                    for producto in ventas_agrupadas:
                        for product in lf.lifestore_products:
                            if(producto[0] == product[0]):
                               ventas_categorias.append([product[3], product[1], product[2], producto[1], (product[2]*producto[1])])
                    
                    
                    #imprimimos las 20 ventas mas alta
                    print("")
                    print("")
                    print("Las 20 mejores ventas generales por número de ejemplares vendidos son:")
                    #ordenamos por número de ventas
                    ventas_categorias.sort(key=lambda x: x[3], reverse=True)
                    for venta in ventas_categorias:
                        if (contador<=20):
                            print("")
                            print("Puesto "+ str(contador))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("Producto: "+venta[1])
                            print("categoría: "+ venta [0])
                            print("Costo unitairio: " + str(venta[2]))
                            print("Número de ventas: "+str(venta[3]))
                            print("Total generado por ventas: "+str(venta[4]))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            contador+=1
                        else:
                            contador=1
                            break
                    print("")
                    print("")
                    print("Las 20 mejores ventas generales por ganancia total son:")
                    #ordenamos por ganancia de ventas
                    ventas_categorias.sort(key=lambda x: x[4], reverse=True)
                    for venta in ventas_categorias:
                        if (contador<=20):
                            print("")
                            print("Puesto "+ str(contador))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("Producto: "+venta[1])
                            print("categoría: "+ venta [0])
                            print("Costo unitairio: " + str(venta[2]))
                            print("Número de ventas: "+str(venta[3]))
                            print("Total generado por ventas: "+str(venta[4]))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            contador+=1
                        else:
                            contador=1
                            break
                    
                    #Obtenemos categorías
                    categorias= []
                    
                    for producto in lf.lifestore_products:
                        if(producto[3] not in categorias):
                            categorias.append(producto[3])
                    categorias.sort()
                    print("")
                    print("")
                    print("Las 20 mejores ventas en cada categoría por número de ventas")
                    ventas_categorias.sort(key=lambda x: x[3], reverse=True)
                    for categoria in categorias:
                        print("")
                        print ("~~~~~~~~~~~~~~~~~~~Para la categoría de "+categoria+"~~~~~~~~~~~~~~")
                        for venta in ventas_categorias:
                            if (contador<=20 and venta[0]==categoria):
                                print("")
                                print("Puesto "+ str(contador))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print("Producto: "+venta[1])
                                print("Costo unitairio: " + str(venta[2]))
                                print("Número de ventas: "+str(venta[3]))
                                print("Total generado por ventas: "+str(venta[4]))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                contador+=1
                        contador=1
                        
                    print("")
                    print("")
                    print("Las 20 mejores ventas en cada categoría por total de ganancia")
                    ventas_categorias.sort(key=lambda x: x[4], reverse=True)
                    for categoria in categorias:
                        print("")
                        print ("~~~~~~~~~~~~~~~~~~~Para la categoría de "+categoria+"~~~~~~~~~~~~~~")
                        for venta in ventas_categorias:
                            if (contador<=20 and venta[0]==categoria):
                                print("")
                                print("Puesto "+ str(contador))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print("Producto: "+venta[1])
                                print("Costo unitairio: " + str(venta[2]))
                                print("Número de ventas: "+str(venta[3]))
                                print("Total generado por ventas: "+str(venta[4]))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                contador+=1
                        contador=1
                    print("")
                    print("")
                    print("Las 20 peores ventas generales por número de ejemplares vendidos son:")
                    #ordenamos por número de ventas
                    ventas_categorias.sort(key=lambda x: x[3])
                    for venta in ventas_categorias:
                        if (contador<=20):
                            print("")
                            print("Puesto "+ str(contador))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("Producto: "+venta[1])
                            print("categoría: "+ venta [0])
                            print("Costo unitairio: " + str(venta[2]))
                            print("Número de ventas: "+str(venta[3]))
                            print("Total generado por ventas: "+str(venta[4]))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            contador+=1
                        else:
                            contador=1
                            break
                    print("")
                    print("")
                    print("Las 20 peores ventas generales por ganancia total son:")
                    #ordenamos por ganancia de ventas
                    ventas_categorias.sort(key=lambda x: x[4])
                    for venta in ventas_categorias:
                        if (contador<=20):
                            print("")
                            print("Puesto "+ str(contador))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("Producto: "+venta[1])
                            print("categoría: "+ venta [0])
                            print("Costo unitairio: " + str(venta[2]))
                            print("Número de ventas: "+str(venta[3]))
                            print("Total generado por ventas: "+str(venta[4]))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            contador+=1
                        else:
                            contador=1
                            break
                    
                    #Obtenemos categorías
                    categorias= []
                    
                    for producto in lf.lifestore_products:
                        if(producto[3] not in categorias):
                            categorias.append(producto[3])
                    categorias.sort()
                    print("")
                    print("")
                    print("Las 20 peores ventas en cada categoría por número de ventas")
                    ventas_categorias.sort(key=lambda x: x[3])
                    for categoria in categorias:
                        print("")
                        print ("~~~~~~~~~~~~~~~~~~~Para la categoría de "+categoria+"~~~~~~~~~~~~~~")
                        for venta in ventas_categorias:
                            if (contador<=20 and venta[0]==categoria):
                                print("")
                                print("Puesto "+ str(contador))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print("Producto: "+venta[1])
                                print("Costo unitairio: " + str(venta[2]))
                                print("Número de ventas: "+str(venta[3]))
                                print("Total generado por ventas: "+str(venta[4]))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                contador+=1
                        contador=1
                        
                   
                    #cambiamos valor para reingresar a la  seleccion de opciones
                    error_seleccion=1
                elif(opc==2):
                    print("")
                    print("Usted selecciono: ")
                    print ("2) Top 20 de productos con mayores busquedas y Top 20 con menores busquedas")
                    productos_buscados=[]
                    categorias=[]
                    contador=1
                    """
                        Creador: Denise Etaira Arias González
                        Función: Creamos una lista con el id del producto y una sumatoria con el numero de 
                                    incidencias de busqueda de aquel producto
                    """
                    for busqueda in lf.lifestore_searches:
                        productos_encontrados=0
                        for producto in productos_buscados:
                            if (busqueda[1]==producto[0]):
                                producto[1] += 1
                                productos_encontrados=1
                                break
                        if(productos_encontrados==0):
                            productos_buscados.append([busqueda[1],1])
                    productos_buscados.sort(key=lambda x: x[1], reverse=True)
                    
                    print("")
                    print("Los 20 productos mas buscados generales")
                    for producto in productos_buscados:
                        for product in lf.lifestore_products:
                            if(producto[0]== product[0]):
                                producto[0]=product[1]
                                producto.append(product[3])
                                break
                    for producto in productos_buscados:
                        if (contador<=20):
                            print("")
                            print("Puesto "+ str(contador))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("Producto: "+producto[0])
                            print("Categoría: "+producto[2])
                            print("Total de busquedas: "+str(producto[1]))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            contador+=1
                        else:
                            contador=1
                            break
                    print("")
                    print("Los 20 productos mas buscados por categoría")   
                    for producto in lf.lifestore_products:
                        if(producto[3] not in categorias):
                            categorias.append(producto[3])
                    categorias.sort()
                    contador=1
                    for categoria in categorias:
                        print("")
                        print ("~~~~~~~~~~~~~~~~~~~Para la categoría de "+categoria+"~~~~~~~~~~~~~~")
                        for produc in productos_buscados:
                            if (contador<=20 and produc[2]==categoria):
                                print("")
                                print("Puesto "+ str(contador))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print("Producto: "+produc[0])
                                print("Total de busquedas: "+str(produc[1]))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                contador+=1
                        contador=1
                        #Menores busquedas
                        productos_buscados.sort(key=lambda x: x[1])
                    
                    print("")
                    print("Los 20 productos menos buscados generales")
                    for producto in productos_buscados:
                        for product in lf.lifestore_products:
                            if(producto[0]== product[0]):
                                producto[0]=product[1]
                                producto.append(product[3])
                                break
                    for producto in productos_buscados:
                        if (contador<=20):
                            print("")
                            print("Puesto "+ str(contador))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("Producto: "+producto[0])
                            print("Categoría: "+producto[2])
                            print("Total de busquedas: "+str(producto[1]))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            contador+=1
                        else:
                            contador=1
                            break
                    print("")
                    print("Los 20 productos menos buscados por categoría")   
                    for producto in lf.lifestore_products:
                        if(producto[3] not in categorias):
                            categorias.append(producto[3])
                    categorias.sort()
                    contador=1
                    for categoria in categorias:
                        print("")
                        print ("~~~~~~~~~~~~~~~~~~~Para la categoría de "+categoria+"~~~~~~~~~~~~~~")
                        for produc in productos_buscados:
                            if (contador<=20 and produc[2]==categoria):
                                print("")
                                print("Puesto "+ str(contador))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print("Producto: "+produc[0])
                                print("Total de busquedas: "+str(produc[1]))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                contador+=1
                        contador=1
                    error_seleccion=1
                elif(opc==3):
                    print("")
                    print("Usted selecciono: ")
                    print ("3) Top 20 de productos con mejores reseñas promedio") 
                    
                    resenias_agrupadas=[]
                    contador=1
                    categorias=[]
                    for venta in lf.lifestore_sales:
                        resenia_encontrado=0
                        for resenia in resenias_agrupadas:
                            if (venta[1]== resenia[0]):
                                resenia[1]+=venta[2]
                                resenia[2]+=1
                                resenia_encontrado=1
                                break
                        if(resenia_encontrado==0):
                            resenias_agrupadas.append([venta[1],venta[2],1])
                    
                    for resenia in resenias_agrupadas:
                        for producto in lf.lifestore_products:
                            if(resenia[0] == producto[0]):
                                resenia[0]=producto[1]
                                resenia.append(producto[3])
                                resenia.append(resenia[1]/resenia[2])
                    resenias_agrupadas.sort(key=lambda x: x[4], reverse=True)  
                    print("")
                    print("Los 20 productos con mejores reseñas promedio generales")
                    for resenia in resenias_agrupadas:
                        if (contador<=20):
                            print("")
                            print("Puesto "+ str(contador))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("Producto: "+resenia[0])
                            print("Categoría: "+resenia[3])
                            print("Número de reseñas: "+str(resenia[2]))
                            print("Calificación promedio en reseñas: "+str(resenia[4]))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            contador+=1
                        else:
                            contador=1
                            break
                    print("")
                    print("Los 20 productos con mejores reseñas promedio por categoría")   
                    for producto in lf.lifestore_products:
                        if(producto[3] not in categorias):
                            categorias.append(producto[3])
                    categorias.sort()
                    for categoria in categorias:
                        print("")
                        print ("~~~~~~~~~~~~~~~~~~~Para la categoría de "+categoria+"~~~~~~~~~~~~~~")
                        for resenia in resenias_agrupadas:
                            if (contador<=20 and resenia[3]==categoria):
                                print("")
                                print("Puesto "+ str(contador))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print("Producto: "+resenia[0])
                                print("Número de reseñas: "+str(resenia[2]))
                                print("Calificación promedio en reseñas: "+str(resenia[4]))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                contador+=1
                        contador=1
                    error_seleccion=1
                    
                elif(opc==4):
                    print("")
                    print("Usted selecciono: ")
                    print ("4) Top 20 de productos con peores reseñas promedio (no devueltos)") 
                        
                    resenias_agrupadas=[]
                    contador=1
                    categorias=[]
                    for venta in lf.lifestore_sales:
                        resenia_encontrado=0
                        devolucion=venta[4]
                        for resenia in resenias_agrupadas:
                            if (venta[1]== resenia[0]):
                                resenia[1]+=venta[2]
                                resenia[2]+=1
                                resenia_encontrado=1            
                                break
                        if(resenia_encontrado==0 and devolucion==0):
                            resenias_agrupadas.append([venta[1],venta[2],1])
                    
                    for resenia in resenias_agrupadas:
                        for producto in lf.lifestore_products:
                            if(resenia[0] == producto[0]):
                                resenia[0]=producto[1]
                                resenia.append(producto[3])
                                resenia.append(resenia[1]/resenia[2])
                    resenias_agrupadas.sort(key=lambda x: x[4])  
                    print("")
                    print("Los 20 productos con peores reseñas promedio generales")
                    for resenia in resenias_agrupadas:
                        if (contador<=20):
                            print("")
                            print("Puesto "+ str(contador))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("Producto: "+resenia[0])
                            print("Categoría: "+resenia[3])
                            print("Número de reseñas: "+str(resenia[2]))
                            print("Calificación promedio en reseñas: "+str(resenia[4]))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            contador+=1
                        else:
                            contador=1
                            break
                    print("")
                    print("Los 20 productoscon peores reseñas promedio por categoría")   
                    for producto in lf.lifestore_products:
                        if(producto[3] not in categorias):
                            categorias.append(producto[3])
                    categorias.sort()
                    for categoria in categorias:
                        print("")
                        print ("~~~~~~~~~~~~~~~~~~~Para la categoría de "+categoria+"~~~~~~~~~~~~~~")
                        for resenia in resenias_agrupadas:
                            if (contador<=20 and resenia[3]==categoria):
                                print("")
                                print("Puesto "+ str(contador))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print("Producto: "+resenia[0])
                                print("Número de reseñas: "+str(resenia[2]))
                                print("Calificación promedio en reseñas: "+str(resenia[4]))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                contador+=1
                        contador=1 
                    error_seleccion=1
                if(opc==5):
                    print("")
                    print("Usted selecciono: ")
                    print ("5) Top 20 de productos con peores reseñas promedio (si devueltos)") 
                        
                    resenias_agrupadas=[]
                    contador=1
                    categorias=[]
                    for venta in lf.lifestore_sales:
                        resenia_encontrado=0
                        devolucion=venta[4]
                        for resenia in resenias_agrupadas:
                            if (venta[1]== resenia[0]):
                                resenia[1]+=venta[2]
                                resenia[2]+=1
                                resenia_encontrado=1            
                                break
                        if(resenia_encontrado==0 and devolucion==1):
                            resenias_agrupadas.append([venta[1],venta[2],1])
                    
                    for resenia in resenias_agrupadas:
                        for producto in lf.lifestore_products:
                            if(resenia[0] == producto[0]):
                                resenia[0]=producto[1]
                                resenia.append(producto[3])
                                resenia.append(resenia[1]/resenia[2])
                    resenias_agrupadas.sort(key=lambda x: x[4])  
                    print("")
                    print("Los 20 productos con peores reseñas promedio generales")
                    for resenia in resenias_agrupadas:
                        if (contador<=20):
                            print("")
                            print("Puesto "+ str(contador))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("Producto: "+resenia[0])
                            print("Categoría: "+resenia[3])
                            print("Número de reseñas: "+str(resenia[2]))
                            print("Calificación promedio en reseñas: "+str(resenia[4]))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            contador+=1
                        else:
                            contador=1
                            break
                    print("")
                    print("Los 20 productoscon peores reseñas promedio por categoría")   
                    for producto in lf.lifestore_products:
                        if(producto[3] not in categorias):
                            categorias.append(producto[3])
                    categorias.sort()
                    for categoria in categorias:
                        print("")
                        print ("~~~~~~~~~~~~~~~~~~~Para la categoría de "+categoria+"~~~~~~~~~~~~~~")
                        for resenia in resenias_agrupadas:
                            if (contador<=20 and resenia[3]==categoria):
                                print("")
                                print("Puesto "+ str(contador))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print("Producto: "+resenia[0])
                                print("Número de reseñas: "+str(resenia[2]))
                                print("Calificación promedio en reseñas: "+str(resenia[4]))
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                contador+=1
                        contador=1
                    error_seleccion=1
                elif(opc==6):
                    print("")
                    print("Usted selecciono: ")
                    print ("6) Total de ingresos y las ventas promedio mensuales")
                    fechas_agrupadas=[]
                    x=0
                    venta=lf.lifestore_sales[0]
                    fecha=venta[3]
                    fecha=fecha[3:5]
                    fechas_agrupadas.append([fecha,0,0])
                    ganancia_venta=0
                    
                    ventas_agrupadas=[] 
                    total_anual=0
                    categorias=[]
                        
                    for sale in lf.lifestore_sales:
                        venta_encontrada=0
                        for venta in ventas_agrupadas:
                            if(venta[0]==sale[1]):
                                venta[1]+=1
                                venta_encontrada=1
                                break
                        if (venta_encontrada==0 ):
                            ventas_agrupadas.append([sale[1],1])
                    
                    
                    for venta in ventas_agrupadas:
                        for producto in lf.lifestore_products:
                            if (venta[0]==producto[0]):
                                total_anual+=(venta[1]*producto[2])
                                break
                        
                    print("El total general es:")   
                    print("     $ "+str(total_anual)) 
                    print("")
                    
                    for venta in lf.lifestore_sales:
                        x+=1
                        fecha=venta[3]
                        fecha=fecha[3:5]
                        existe_fecha=0
                        
                        for fechas in fechas_agrupadas:
                            if(fechas[0]==fecha):
                                fechas[1]+=1
                                for producto in lf.lifestore_products:
                                    if(venta[1] == producto[0]):
                                        fechas[2]+= producto[2]
                                existe_fecha=1
                                break
                                
                        if(existe_fecha == 0):
                            for producto in lf.lifestore_products:
                                    if(venta[1] == producto[0]):
                                        ganancia_venta= producto[2]
                            fechas_agrupadas.append([fecha,1,ganancia_venta])
                    fechas_agrupadas.sort(key=lambda x: x[0])
                    for fechas in fechas_agrupadas:
                        if(fechas[0]=="01"):
                            print("Ventas de Enero: ")
                        elif(fechas[0]=="02"):
                            print("Ventas de Febrero: ")
                        elif(fechas[0]=="03"):
                            print("Ventas de Marzo: ")
                        elif(fechas[0]=="04"):
                            print("Ventas de Abril: ")
                        elif(fechas[0]=="05"):
                            print("Ventas de Mayo: ")
                        elif(fechas[0]=="06"):
                            print("Ventas de Junio: ")
                        elif(fechas[0]=="07"):
                            print("Ventas de Julio: ")
                        elif(fechas[0]=="08"):
                            print("Ventas de Agosto: ")
                        elif(fechas[0]=="09"):
                            print("Ventas de Septiembre: ")
                        elif(fechas[0]=="10"):
                            print("Ventas de Octubre: ")
                        elif(fechas[0]=="11"):
                            print("Ventas de Noviembre: ")
                        elif(fechas[0]=="12"):
                            print("Ventas de Diciembre: ")
                        print("     Número de ventas: "+ str(fechas[1]))
                        print("     Total ingreso del mes: " + str(fechas[2]))
                        print("     Promedio del mes: "+str(fechas[2]/fechas[1]))
                    print("Si algun mes no fue mencionado anteriormente fue debido a que no se reportó ninguna venta en dicho mes")
                    error_seleccion=1
                    
                elif(opc==7):
                    print("")
                    print("Usted selecciono: ")
                    print ("7) Total anual y meses con mas ventas")
                    year = str(dt.now())
                    year=year[:4]   
                    ventas_agrupadas=[] 
                    total_anual=0
                    categorias=[]
                    fechas_agrupadas=[]
                    contador=1
                        
                    for sale in lf.lifestore_sales:
                        anio=sale[3]
                        anio=anio[6:]
                        venta_encontrada=0
                        for venta in ventas_agrupadas:
                            if(venta[0]==sale[1]):
                                venta[1]+=1
                                venta_encontrada=1
                                break
                        if (venta_encontrada==0 and anio==year):
                            ventas_agrupadas.append([sale[1],1])
                    
                    
                    for venta in ventas_agrupadas:
                        for producto in lf.lifestore_products:
                            if (venta[0]==producto[0]):
                                total_anual+=(venta[1]*producto[2])
                                break
                        
                    print("El total general del año " + year+" es:")   
                    print("     $ "+str(total_anual))
                    print("")
                    print ("El total por categoria es: ")
                    for producto in lf.lifestore_products:
                        if(producto[3] not in categorias):
                            categorias.append(producto[3])
                    categorias.sort()
                    for categoria in categorias:
                        total_anual=0
                        print("")
                        print ("~~~~~~~~~~~~~~~~~~~Para la categoría de "+categoria+"~~~~~~~~~~~~~~")
                        for venta in ventas_agrupadas:
                            for producto in lf.lifestore_products:
                                if (venta[0]==producto[0] and producto[3]==categoria):
                                    total_anual+=(venta[1]*producto[2])
                                    break
                        print ("       Total $ "+str(total_anual))
                        
                    for venta in lf.lifestore_sales:
                        fecha=venta[3]
                        fecha=fecha[3:5]
                        existe_fecha=0
                        
                        for fechas in fechas_agrupadas:
                            if(fechas[0]==fecha):
                                fechas[1]+=1
                                for producto in lf.lifestore_products:
                                    if(venta[1] == producto[0]):
                                        fechas[2]+= producto[2]
                                existe_fecha=1
                                break
                                
                        if(existe_fecha == 0):
                            for producto in lf.lifestore_products:
                                    if(venta[1] == producto[0]):
                                        ganancia_venta= producto[2]
                            fechas_agrupadas.append([fecha,1,ganancia_venta])
                    fechas_agrupadas.sort(key=lambda x: x[2], reverse=True )
                    print("")
                    print("Los 4 meses con mejores ventas")
                    for fechas in fechas_agrupadas:
                        if(contador<=4):
                            print("")
                            print("Puesto "+ str(contador))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            if(fechas[0]=="01"):
                                print("Ventas de Enero: ")
                            elif(fechas[0]=="02"):
                                print("Ventas de Febrero: ")
                            elif(fechas[0]=="03"):
                                print("Ventas de Marzo: ")
                            elif(fechas[0]=="04"):
                                print("Ventas de Abril: ")
                            elif(fechas[0]=="05"):
                                print("Ventas de Mayo: ")
                            elif(fechas[0]=="06"):
                                print("Ventas de Junio: ")
                            elif(fechas[0]=="07"):
                                print("Ventas de Julio: ")
                            elif(fechas[0]=="08"):
                                print("Ventas de Agosto: ")
                            elif(fechas[0]=="09"):
                                print("Ventas de Septiembre: ")
                            elif(fechas[0]=="10"):
                                print("Ventas de Octubre: ")
                            elif(fechas[0]=="11"):
                                print("Ventas de Noviembre: ")
                            elif(fechas[0]=="12"):
                                print("Ventas de Diciembre: ")
                            print("     Número de ventas: "+ str(fechas[1]))
                            print("     Total ingreso del mes: " + str(fechas[2]))
                            print("     Promedio del mes: "+str(fechas[2]/fechas[1]))
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            contador+=1
                        else:
                            break
                    error_seleccion=1  
            break
        else:
            error_usuario=1
    if((user!="0" and contrasenia!="0") and error_usuario==1):
        print ("------------------------------------------------------------------------------------------------")
        print("Usuario y/o contraseña invalido \nPor favor escriba un usuario y contraseña validos \nO si decea salir ingrese unicamente 0 en el usuario y contraseña")
        print ("------------------------------------------------------------------------------------------------")

print ("El programa ha finalizado")