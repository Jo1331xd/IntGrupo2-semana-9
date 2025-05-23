matriz = [["Roger ", "Eduardo ", "Zahid "], 
          ["Cesar ", "Luis ", "Andres "], 
          ["Rene ", "Edgar ", "Carlitos"]]

cant_letras= []

print("-"*45) 
for fila in matriz: 
    for columna in fila:
        print(f"| {columna:>10}", end = " ") 
    print("|") 
print("-"*45)   

for fila in matriz:
    
    new_row = []
    
    for columna in fila:
        new_row.append(len(columna))
    cant_letras.append(new_row)
        
print("-"*26) 
for fila in cant_letras: 
    for columna in fila:
        print(f"| {columna:>5}", end = " ") 
    print(" |") 
print("-"*26) 

#programa especializado en contar e imprimicar sus caracteres en numeros