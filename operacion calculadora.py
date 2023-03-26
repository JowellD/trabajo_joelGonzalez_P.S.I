def suma(numero_1,numero_2):
    return numero_1+numero_2
def resta(numero_1,numero_2):
    return numero_1-numero_2
def multiplicacion(numero_1,numero_2):
    return numero_1*numero_2
def division(numero_1,numero_2):
    if numero_1>0 and numero_2>0:
        return numero_1/numero_2
    else: 
        print("Sintax Error")
def operacion(numero_1,caracter,numero_2):
    if caracter=="+":
        solucion=suma(numero_1,numero_2)
        print(f"{numero_1} + {numero_2}= {solucion}")
    elif caracter=="-":
        solucion=resta(numero_1,numero_2)
        print(f"{numero_1} - {numero_2}= {solucion}")
    elif caracter=="*":
        solucion=multiplicacion(numero_1,numero_2)
        print(f"{numero_1} * {numero_2}= {solucion}")
    elif caracter=='/':
        solucion=division(numero_1,numero_2)
        print(f'{numero_1} / {numero_2}= {solucion}')
    else:
       print('error')

    

x=int(input("digite el primer digito: "))
sing=str(input("digite la operacion a seguir: "))
y=int(input("digite el segundo digito: "))
total=operacion(x,sing,y)