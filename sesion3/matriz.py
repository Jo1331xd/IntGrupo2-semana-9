#MATRIZ 
matriz = [[10, 2], [300, 4]]
print("-"*17)
for fila in matriz: 
    for columna in fila:
        print(f"| {columna:>3}", end = " ") #El end es para hacer un salto de pagina/ a su vez esta el formato para alinear
        #los digitos ingresados y que queden parejo
        
    print("|") #En eses print podes ponerle algo a la par para formar la tabla
print("-"*17)                                                                         

