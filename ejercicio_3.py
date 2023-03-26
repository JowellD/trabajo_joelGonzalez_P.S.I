"""ejercicio 21
El área de un triángulo puede calcularse mediante la siguiente fórmula, en la que b es la
longitud de la base del triángulo, y h es su altura:
área = (b * h)/2
Escribe un programa que permita al usuario introducir los valores de b y h. El programa
debe calcular y mostrar el área de un triángulo de base b y altura h."""
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

base=float(input("ingrese el valor asignado a la base del triangulo: "))
altura=float(input("ingrese el valor asignado a la altura del triangulo: "))
area=area_triangulo(base,altura)
print(f"el area del triangulo cuya base es: {base} y altura es: {altura}: {area}")