"""ejercicio 100
Escribe una función que determine cuántos días hay en un mes concreto. La función
tomará dos parámetros: El mes como un entero entre 1 y 12, y
el año como un número entero de cuatro dígitos. Asegúrese de que su función informa del número correcto
de días en febrero para los años bisiestos. Incluya un programa principal que lea un mes y un año del usuario y muestre el número de días en febrero para los años bisiestos.
año del usuario y muestre el número de días de ese mes. Puede que su
del Ejercicio 57 para resolver este problema"""

meses = {
    1:"enero",2:"febrero",3:"marzo",4:"abril",
    5:"mayo",6:"junio",7:"julio",8:"agosto",
    9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"

}
from ejercicio_10 import *
from ejercicio_7 import *
def dias_del_mes(mes,año):
    bisiest_o_no=bisiesto(año)
    if mes<=12:
        if meses[mes]=="febrero":
            if bisiest_o_no=="es bisiesto":
             dias=29
            else:
                dias=28
        else:
            mes_=meses[mes]
            dias=dias_mes(mes_)
        return dias


mes=int(input("digite el mes: "))
año=int(input("digite el año: "))
resultado=dias_del_mes(mes,año)
print(f" el mes {meses[mes]} tiene {resultado} dias")    

         

