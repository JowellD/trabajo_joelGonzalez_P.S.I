"""ejercicio 7
Escriba un programa que lea un número entero positivo, n, del usuario y luego muestre la suma de todos los números enteros de 1 a n. La suma de los primeros n números enteros positivos se puede calcular de la siguiente manera
suma de todos los enteros de 1 a n. La suma de los primeros n enteros positivos se puede
utilizando la fórmula:
                        sum=(n*(n+1))/2
"""
def suma_enteros_N(numero):
    suma_enteros=(numero*(numero+1))/2
    print(f"la suma de los numeros enteros del  {numero} es : {suma_enteros}")


s=int(input("digite un numero entero positivo: "))
prueba=suma_enteros_N(s)

