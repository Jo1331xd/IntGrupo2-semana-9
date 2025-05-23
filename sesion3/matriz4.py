matriz = [[10, 20], [30, 40]]
print("-"*17)
for fila in matriz: 
    for columna in fila:
        print(f"| {columna:>3}", end = " ")
    print("|") 
print("-"*17) 


escalar = 1.15
matriz_escalada = [[float(valor * escalar) for valor in fila] for fila in matriz]

print("-"*17)
for fila in matriz_escalada: 
    for columna in fila:
        print(f"| {columna:>3.2f}", end = " ")
    print("|") 
print("-"*17)


