
import os
import random
import time

participantes= list()
while True:
    os.system("cls||clear")
    os.system("color b1")
    nombre = input("Ingrese el nombre del participantes (o 'fin' para terminar):")
    if nombre.lower() == 'fin':
        break
    participantes.append(nombre.upper())
    print("Participante agregado...")
    print(participantes)
    
os.system("cls || clear ")
print("Participantes Registrado")
print(participantes)
print(input("Presione una tecla"))
cont =10

for cont in range (10,0, -1): #Se puede hacer para hacer un hacer un hacer un contador hacer 
    
    os.system("cls||clear") #contador
    print(cont)
    time.sleep(1)
os.system("cls||clear")

fin = len(participantes) - 1
ganador= random.randit(0,fin)
print(f"ganador: {participantes[ganador]}")

