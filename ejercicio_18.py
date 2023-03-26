"""ejercicio 92
Un número primo es un número entero mayor que 1 que sólo es divisible por uno y por sí mismo.
Escribe una función que determine si su parámetro es primo o no, devolviendo
True en caso afirmativo y False en caso contrario. Escribe un programa principal que lea un número entero
del usuario y muestre un mensaje indicando si es primo o no. Asegúrese de que
que el programa principal no se ejecute si el archivo que contiene la solución se importa en otro programa.
en otro programa."""

def es_primo(numero):
    if numero>2:
        for i in range(2,numero):
            if numero%i==0:
                return False
        return True
    else:
        return False
    
numero=int(input("ingrese un numero: "))
if es_primo(numero):
    print(f" el numero {numero} es primo")
else:
     print(f" el numero {numero} no es primo")