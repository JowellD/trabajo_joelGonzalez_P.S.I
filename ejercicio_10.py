"""ejercicio 57
La mayoría de los años tienen 365 días. Sin embargo, el tiempo necesario para que la Tierra orbite alrededor del Sol
es ligeramente superior. Por ello, en algunos años se incluye un día más, el 29 de febrero, para corregir esta diferencia.
para corregir esta diferencia. Estos años se denominan bisiestos.
Las reglas para determinar si un año es bisiesto o no son las siguientes:
- Todo año divisible por 400 es bisiesto.
- De los años restantes, cualquier año divisible por 100 no es bisiesto.
- De los años restantes, cualquier año divisible por 4 es bisiesto.
- Todos los demás años no son bisiestos.
Escribe un programa que lea un año del usuario y muestre un mensaje indicando
si es o no bisiesto"""

def bisiesto(año):
    if año%400==0:
        esaño="es bisiesto"
    elif año%4==0:
        esaño="es bisiesto"
    elif año%100==0:
        esaño="no es bisiesto"
    else:
        esaño="no es bisiesto"
    return esaño

"""año=int(input("ingrese el año: "))
resultado=bisiesto(año)
print(f"el año {año} {resultado}")"""
