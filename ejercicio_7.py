"""ejercicio 38
La duración de un mes varía entre 28 y 31 días. En este ejercicio crearás
un programa que lea del usuario el nombre de un mes en forma de cadena. Luego tu
programa debe mostrar el número de días de ese mes. Muestre "28 o 29 días"
para febrero, de forma que se tengan en cuenta los años bisiestos."""

def dias_mes(mes):
    dias=31
    if mes=="abril" or mes=="junio" or mes=="septiembre" or mes=="noviembre":
        dias=30
    elif mes=="febrero":
        dias=" 28 o 29 "

    return dias

"""mes=str(input("ingrese el mes: "))
resultado=dias_mes(mes)
print(f"el mes de {mes} tiene {resultado} dias")"""