"""ejercicio 37
Escribe un programa que determine el nombre de una figura a partir de su número de lados. Lee
el número de lados del usuario y luego informar el nombre apropiado como parte de
un mensaje significativo. El programa debe admitir formas con un número de lados comprendido entre 3
hasta (e incluyendo) 10 lados. Si se introduce un número de lados fuera de este rango
entonces su programa debe mostrar un mensaje de error apropiado."""

def tipo_figura(lados):
    if lados < 3:
        return "No válida"
    elif lados == 3:
        return "Triángulo"
    elif lados == 4:
        return "Cuadradao"
    elif lados == 5:
        return "Pentágono"
    elif lados == 6:
        return "Hexágono"
    elif lados == 7:
        return "Heptágono"
    elif lados == 8:
        return "Octágono"
    elif lados == 9:
        return "Eneágono"
    elif lados == 10:
        return "Decágono"
    else:
        return "Polígono con más de 10 lados"
    
lados=int(input("ingrese los lados de su figura: "))
resultado=tipo_figura(lados)
if(resultado=="No válida"):
    print(" una figura de dos lado no existe")
else:
    print(f"su figura es {resultado}")