matriz = [["Roger ", "Eduardo ", "Zahid "], ["Cesar ", "Luis ", "Andres "], ["Rene ", "Edgar ", "Carlitos"]]
print("-"*50) #Techo arriba
for fila in matriz: 
    for columna in fila:
        print(f"| {columna:>10}", end = " ") #de aqui cierro el otro lado
    print("|") #De aqui cierro la parte de la tabla vertical
print("-"*50)   #Techo abajo

