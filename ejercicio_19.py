"""ejercicio 98
Escribe dos funciones, hex2int e int2hex, que conviertan entre dígitos hexadecimales
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E y F) y enteros de base 10. La función
hex2int se encarga de convertir una cadena que contiene un solo dígito hexadecimal en un entero de base 10, mientras que la función int2hex se encarga de convertir un entero entre 0 y 15 en un solo dígito hexadecimal. Cada función
tomará el valor a convertir como único parámetro y devolverá el valor convertido
como único resultado de la función. Asegúrese de que la función hex2int funciona correctamente para
tanto para mayúsculas como para minúsculas. Sus funciones deben terminar el programa con un
mensaje de error significativo si se proporciona un parámetro no válido"""

# Diccionario de equivalencia de dígitos hexadecimales y decimales
equivalencias_hexadecimales = {
    "0": 0, "1": 1, "2": 2, "3": 3,
    "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "A": 10, "B": 11,
    "C": 12, "D": 13, "E": 14, "F": 15,
    "a": 10, "b": 11, "c": 12, "d": 13,
    "e": 14, "f": 15
}
equivalencias_decimales={
    0:"0",1: "1", 2: "2", 3: "3",
    4: "4", 5: "5", 6: "6", 7: "7",
    8: "8", 9: "9",  10:"A", 11:"B",
    12:"C", 13:"D", 14:"E", 15:"F",
}

def decimal_hexadecimal(dig):
    if dig<15:
        return equivalencias_decimales[dig]
    else:
        print("no existe en hexadecimal")
        return -1
def hexadecimal_decimal(dig_hexadecimal):
    if dig_hexadecimal!=("a","b","c","d","e","f"):
        print("no existe esta conversion")
        return -1
    else:
        return equivalencias_hexadecimales[dig_hexadecimal]
         
decimal =int(input("digite un numero:"))
hexadecimal =input("digite un numero o carater hexadecimal :")

resultado = decimal_hexadecimal(decimal)
print(f"{decimal} en hexadecimal es {resultado}")
resultado = hexadecimal_decimal(hexadecimal)
print(f"{hexadecimal} en decimal es {resultado}")
