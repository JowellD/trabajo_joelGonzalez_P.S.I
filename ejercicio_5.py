"""ejercicio 16
Escribe un programa que comience leyendo un radio, r, del usuario. El programa
el área de un círculo de radio r y el volumen de una esfera de radio r.
volumen de una esfera de radio r. Utiliza la constante pi del módulo matemático en tus cálculos.
cálculos.
Sugerencia: El área de un círculo se calcula utilizando la fórmula área = πr 2. El volumen de una esfera en
volumen de una esfera se calcula mediante la fórmula volumen = 4/3 πr^3."""

from math import pi
def area_volumen_esfera(radio):
    area=pi*(radio*radio)
    volumen=(4/3)*(pi)*(pow(radio,3))
    print("el area de la esfera es %f y su volumen es %f"%(area,volumen))

radio=float(input("ingrese el radio de la esfera: "))
area_volumen=area_volumen_esfera(radio)
