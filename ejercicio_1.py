"""ejercicio #7
El programa que cree para este ejercicio comenzará leyendo el coste de una comida
pedida en un restaurante por el usuario. A continuación, el programa calculará los impuestos y
propina de la comida. Utilice el tipo impositivo local para calcular la cantidad de impuestos a pagar.
Calcule la propina como el 18% del importe de la comida (sin impuestos). La salida de
programa debe incluir el importe del impuesto, el importe de la propina y el total general de la comida, incluidos el impuesto y la propina.
de la comida, incluidos los impuestos y la propina. Formatee la salida para que todos los valores
se muestren con dos decimales"""
def costocomida():
    tasa_impuestos=0.18
    tasa_propina=0.07
    costo=float(input("ingrese el costo estandar del la comida: "))
    impuestos=costo*tasa_impuestos
    propina=costo*tasa_propina
    total=costo+impuestos+propina
    print(f"el impuesto es {impuestos} y la propina es {propina} haciendo el total {total} ")


s=costocomida()
print(s)