"""ejercicios 67
Cada zoo determina el precio de la entrada en función de la edad del visitante.
Los visitantes menores de 2 años entran gratis. Los niños de entre 3 y
12 años cuestan 14 $. Los mayores de 65 años cuestan 18,00 $. Admisión
para el resto de invitados cuesta 23,00 $.
Cree un programa que comience leyendo las edades de todos los invitados de un grupo
del usuario, con una edad ingresada en cada línea. El usuario introducirá una línea en blanco para
en blanco para indicar que no hay más huéspedes en el grupo. A continuación, el programa debe mostrar
el coste de la entrada para el grupo con un mensaje apropiado. El precio
con dos decimales"""

def precio_zoo():
    edad=input("ingrese su edad: ")
    while edad!="":
        edad=int(edad)
        if edad<=2:
            total=0.00
        elif edad<=12:
            total=14.00
        elif edad <=64:
            total=23.00
        else:
            total=18.00
        
        return total

resultado=precio_zoo()
print(f" el total es {resultado}")