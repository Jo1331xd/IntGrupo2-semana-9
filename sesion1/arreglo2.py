#Arreglos de tipo entero

array_int= [5, 4, 9, 2, 1]

#Ordenar el arreglo de menor a mayor
array_int.sort()
print("Array de enteros ordenado: ", array_int)

#Ordenar el arreglo de menor a mayor
array_int.sort(reverse=True)

print("Array de enteros ordenados de mayor a menor", array_int)


#Buscar un elemento en el arreglo
elemento=4
if elemento in array_int:
    print(f"El elemento {elemento} se encuentre en el arreglo. ")
else:
    print(f"El elemento {elemento} no encuentra en el arreglo. ")

#insertar un elemento en el arreglo
array_int.append(6)
print("Array de enteros despu+es de insertar 6:", array_int)
