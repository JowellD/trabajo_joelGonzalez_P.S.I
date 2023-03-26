"""ejercicio 82
En una jurisdicción determinada, las tarifas de taxi consisten en una tarifa base de 4,00 $, más 0,25
por cada 140 metros recorridos. Escribe una función que tome la distancia recorrida (en
kilómetros) como único parámetro y devuelva la tarifa total como único resultado. Escriba un programa
programa principal que demuestre la función"""

def calcula_tarifa_taxi(recorrido):
    tarifa=4.00
    total=tarifa+(0.25*recorrido)
    return total

recorrido=float(input("ingrese los kilometros recorridos: "))
resultado=calcula_tarifa_taxi(recorrido)
print(f"total a pagar : ${resultado}")
