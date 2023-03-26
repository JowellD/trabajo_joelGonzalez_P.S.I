def tabla_impares():
    for i in range(1,11,2):
        if i%2==1:
            print("tabla del ", i)
            print("____________________")
            for j in range(1,11):
                print (i,"*",j,"=",i*j)
                print("____________________")
def tabla_pares():
    for i in range(1,11):
        if i%2==0:
            print("tabla del ", i)
            print("____________________")
            for j in range(1,11):
                print (i,"*",j,"=",i*j)
                print("____________________")


opcion = str(input("Ingrese la opción deseada: "))
if opcion == 'pares'or opcion == 'PARES':
    x=tabla_pares()

elif opcion == 'impares' or opcion == 'IMPARES':
   x=tabla_impares()
else:
    print("Opción inválida")