def tablas_multiplicar():
    print("    ",end="")
    for i in range(1,11,1):
        print(f"   {i}", end="")
    print()
    for i in range(1,11,1):
        print(f"   {i}", end="")
        for j in range(1,11,1):
            print("%4d" % (i*j), end="")
        print()
    
resutado=tablas_multiplicar()
