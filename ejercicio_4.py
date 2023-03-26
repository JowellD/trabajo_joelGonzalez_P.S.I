"""ejercicio 22
En el ejercicio anterior creaste un programa que calculaba el área de un triángulo
conociendo la longitud de la base y la altura. También es posible calcular
el área de un triángulo cuando se conocen las longitudes de los tres lados. Sean s1, s2 y s3
las longitudes de los lados. Sea s = (s1 + s2 + s3)/2. El área del triángulo
se puede calcular mediante la siguiente fórmula:
área =s * (s - s1) * (s - s2) * (s - s3)
Desarrolla un programa que lea del usuario las longitudes de los lados de un triángulo y
y muestre su área."""
from math import sqrt

def area_triangulo_v2(lado1,lado2,lado3):
    s=(lado1+lado2+lado3)/2
    area=sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
    return area

lado_1=float(input("primer lado del triangulo: "))
lado_2=float(input("primer lado del triangulo: "))
lado_3=float(input("primer lado del triangulo: "))
area=area_triangulo_v2(lado_1,lado_2,lado_3)
print(f"el area del triangulo es : {area}")