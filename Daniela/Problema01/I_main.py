#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:09:40 2019

@author: Daniela
"""
import I_aritmetica as fc
import sys

N= input("Ingrese un numero entero: ")

N = int(N)

validacion = fc.ingreso_N(N)
if (validacion == True):
    suma=fc.suma_pares(N)
    cantidad=fc.cantidad_pares(N)
    promedio=fc.media_aritmetica(N)

    print ("La suma de los numeros pares es: ", suma)
    print ("El total de numeros sumados es: ", cantidad)
    print ("La media aritmetica de los numeros impares es: ", promedio )

