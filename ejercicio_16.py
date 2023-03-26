"""ejercicio 81
Escribe una función que tome las longitudes de los dos lados menores de un triángulo rectángulo como
sus parámetros. Devuelve como resultado de la función la hipotenusa del triángulo, calculada mediante el
como resultado de la función. Incluye un programa principal que lea las longitudes de
los lados más cortos de un triángulo rectángulo del usuario, utiliza su función para calcular la longitud de la hipotenusa, y devuelve como resultado la hipotenusa.
longitud de la hipotenusa y muestre el resultado"""
from math import sqrt
def calcular_hipotenusa(lado1,lado2):
    hipotenusa=sqrt((lado1**2)+(lado2**2))
    return hipotenusa

cateto=float(input("ingrese el primer cateto: "))
cateto2=float(input("ingrese el segundo cateto: "))
resutado=calcular_hipotenusa(cateto,cateto2)
print(f"la hipotenusa del trangulo es: {resutado}")
