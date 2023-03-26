"""ejercicio 63
Escribe un programa que muestre una tabla de conversión de temperatura para grados Celsius y
grados Fahrenheit. La tabla debe incluir filas para todas las temperaturas entre 0
y 100 grados Celsius que sean múltiplos de 10 grados Celsius. Incluye
en las columnas."""

def tabla_celsiud_a_farenheit():
    for celsius in range (0,101,10):
        farenheit=(celsius*1.8)+32
        print(f"{celsius} = {farenheit}")

resultado=tabla_celsiud_a_farenheit()
