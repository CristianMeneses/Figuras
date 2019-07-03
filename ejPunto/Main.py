# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:26:27 2019

@author: sebastian
"""

import Circulo
import Cuadrado
import Triangulo
import Rectangulo
import Elipse
import Figura
import Punto

class Main:
    
    puntoOrigen = Punto()
    puntoFin = Punto()
    Figura = f
    print('1.Circulo\n2.Cuadrado\n3.Triangulo\n4.Rectangulo\n5.Elipse')
    print('Elija una opcion: ')
    int(input(opc))
    
    if opc == 1:
        print('Trabajando con Circulo: ')
        f = Circulo()
        puntoOrigen.setX(0)
        puntoOrigen.setY(0)
        puntoFin.setX(5)
        puntoFin.setY(0)
        mostrar(f, puntoOrigen, fin)
    elif opc == 3:
        print('Trabajando con Triangulo: ')
        f = Triangulo()
        puntoOrigen.setX(0)
        puntoOrigen.setY(0)
        puntoFin.setX(5)
        puntoFin.setY(0)
        mostrar(f, puntoOrigen, puntoFin)    
    elif opc == 2:
        print('Trabajando con Cuadrado: ')
        f = Cuadrado()
        puntoOrigen.setX(0)
        puntoOrigen.setY(0)
        puntoFin.setX(5)
        puntoFin.setY(0)
        mostrar(f, puntoOrigen, puntoFin)        
    elif opc == 4:
        print('Trabajando con Rectangulo: ')
        f = Rectangulo()
        puntoOrigen.setX(0)
        puntoOrigen.setY(0)
        puntoFin.setX(5)
        puntoFin.setY(0)
        mostrar(f, puntoOrigen, puntoFin)
    elif opc == 5:
        print('Trabajando con Elipse: ')
        f = Elipse()
        puntoOrigen.setX(0)
        puntoOrigen.setY(0)
        puntoFin.setX(5)
        puntoFin.setY(0)
        mostrar(f, puntoOrigen, puntoFin)        
        
def mostrar():
    f.