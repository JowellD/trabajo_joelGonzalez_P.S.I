"""ejercicio 72
Una cadena es palíndroma si es idéntica hacia delante y hacia atrás. Por ejemplo "anna",
"civic", "level" y "hannah" son ejemplos de palabras palindrómicas.Escriba un programa
que lea una cadena del usuario y utilice un bucle para determinar si es o no un palíndromo.
palíndromo. Muestre el resultado, incluyendo un mensaje de salida significativo"""

def palindromo(dato):
    es_palindromo=True

    for i in range(0,len(dato)//2):
        if dato[i]!=dato[len(dato)-i-1]:
            es_palindromo=False
    
    if es_palindromo:
        print(f"{dato} es palindromo ")
    else:
        print(f"{dato} no es palindromo ")

dato=input("digite un numero o nombre: ")
resultado=palindromo(dato)
