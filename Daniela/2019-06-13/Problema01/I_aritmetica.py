#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 19:17:42 2019

@author: Universidad
"""

limite = 1000

def ingreso_N(N):
        if N<1 or N>limite:
                print("Ingresar un numero mayor que 1 y menor que 1000")
                return False;
        else:
                return True;

def suma_pares(N):
        suma_par = 0
        for i in range(N,limite + 1):
                if (i%2 == 0):
                        suma_par = suma_par + i
        return suma_par;
        
def cantidad_pares(N):
        cant_par = 0
        for i in range (N,limite + 1):
                if (i%2 == 0):
                        cant_par = cant_par + N
        return cant_par;
            
def media_aritmetica(N):
        suma_impar = 0
        cant_impar = 0
        for i in range(N,limite + 1):
                if (i%2 == 1):
                        suma_impar = suma_impar + i
                        cant_impar = cant_impar + 1

        resultado = 0
        if (cant_impar < 1):
                resultado = "Error: No se encontraron numeros impares."
        else:
                resultado = suma_impar / cant_impar

        return resultado;
        
    