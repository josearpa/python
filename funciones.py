#!/usr/bin/python
# -*- coding: utf-8 -*-
#En este archivo vamos a crear varias funcionesself.
from subprocess import call

##Maximo.  En esta funcion vamos a recibir dos numeros y vamos a devolver el mayorself.
def maximo(uno, dos):
    if int(uno) > int(dos) :
        return uno
    else:
        return dos

def menu(nombre):
    call("clear")
    print "Hola " + nombre + "...\nPor favor escribe un numero"
    number1 = raw_input()
    print "Ahora escribe otro numero."
    number2 = raw_input()
    print "El numero mayor entre " + number1 + " y " + number2 + " es: \n" + maximo(number1, number2)

menu("Jose")
