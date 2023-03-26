"""ejercicio 36 
En este ejercicio crearás un programa que lea una letra del alfabeto del
usuario. Si el usuario introduce a, e, i, o o u entonces su programa debe mostrar un mensaje
indicando que la letra introducida es una vocal. Si el usuario introduce y, el programa
debe mostrar un mensaje indicando que a veces y es una vocal y a veces y es una consonante.
una consonante. En caso contrario, el programa debe mostrar un mensaje que indique que la letra introducida es una consonante.
es una consonante."""

def vocal_o_consonante(letra):
    if letra=="a" or letra=="A"\
    or letra=="e"or letra=="E"\
    or letra=="i" or letra=="I"\
    or letra=="o" or letra=="O"\
    or letra=="u" or letra=="U":
        print(f"la letra {letra} es una vocal ")
    elif letra=="y" or letra=="Y":
        print(f" esta letra {letra} aveces funciona como vocal y aveces como consonante")
    else:
        print(f"la letra {letra} es una consonante")

letra=str(input("digite una letra: "))
vocal_o_consonante(letra)