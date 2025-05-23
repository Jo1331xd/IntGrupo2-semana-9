#Matriz ejercicio ingresarle numeros flotantes o decimales

matriz = [[1.5, 2.5], [3.5, 4.5]]
print("-"*17)
for fila in matriz: 
    for columna in fila:
        print(f"| {columna:>3.1f}", end = " ") 
    print("|") 
print("-"*17)               