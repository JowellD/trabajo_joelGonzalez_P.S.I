"""ejercicio 73
Hay numerosas frases que son palíndromos cuando se ignora el espaciado. Ejemplos
incluyen "go dog", "flee to me remote elf" y "some men interpret nine memos",
entre muchas otras. Amplíe su solución al Ejercicio 72 para que ignore el espaciado
al determinar si una cadena es o no un palíndromo. Para un reto adicional,
amplíe su solución para que también ignore los signos de puntuación y trate las mayúsculas
y minúsculas como equivalentes"""

def palindromo(dato):
    dato=dato.lower().replace(" ","") 
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