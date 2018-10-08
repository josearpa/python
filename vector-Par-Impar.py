#!/usr/bin/python
# -*- coding: utf-8 -*-
#codigo para manejar vectores con operaciones matemáticasself.
par = [2,4,6,8]
impar = [1,3,5,7,9]
resultado = 0
print "Qué operacion matemática vas a realizar."
print "1. Suma"
print "2. Resta"
print "3. Multiplicación"
print "4. División"
opcion = raw_input()
if opcion == "1":
    print "Suma"
    print "¿Qué posición del vector par va a seleccionar?"
    PosicionPar = raw_input()
    print "¿Qué posición del vector impar va a seleccionar?"
    PosicionImpar = raw_input()
    suma=par[int(PosicionPar)]+impar[int(PosicionImpar)]
    print suma
elif opcion == "2":
    print "Resta"
    print "¿Qué posición del vector par va a seleccionar?"
    PosicionPar = raw_input()
    print "¿Qué posición del vector impar va a seleccionar?"
    PosicionImpar = raw_input()
    resta=par[int(PosicionPar)]-impar[int(PosicionImpar)]
    print resta
elif opcion == "3":
    print "Multiplicación"
    print "¿Qué posición del vector par va a seleccionar?"
    PosicionPar = raw_input()
    print "¿Qué posición del vector impar va a seleccionar?"
    PosicionImpar = raw_input()
    Multiplicacion=par[int(PosicionPar)]*impar[int(PosicionImpar)]
    print Multiplicacion
elif opcion == "4":
    print "División"
    print "¿Qué posición del vector par va a seleccionar?"
    PosicionPar = raw_input()
    print "¿Qué posición del vector impar va a seleccionar?"
    PosicionImpar = raw_input()
    division=par[int(PosicionPar)]/impar[int(PosicionImpar)]
    print division
else:
    print "Opción no válida"
