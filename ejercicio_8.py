"""ejercicio 40
Un triángulo puede clasificarse en equilátero, isósceles o escaleno en función de la longitud de sus lados.
o escaleno. Los 3 lados de un triángulo equilátero tienen la misma longitud. Un triángulo isósceles
isósceles tiene dos lados de la misma longitud y un tercer lado de longitud diferente.
diferente. Si todos los lados tienen longitudes diferentes, el triángulo es escaleno.
Escribe un programa que lea del usuario las longitudes de los 3 lados de un triángulo.
Muestra un mensaje indicando el tipo de triángulo."""

def tipo_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3 :
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")

lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))
resultado=tipo_triangulo(lado1,lado2,lado3)