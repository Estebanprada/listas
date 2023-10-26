# Inicializa dos listas vacías para almacenar los nombres de los aprendices y sus edades.
aprendices = []
edades = []
max_aprendices = 4 # Máximo de 4 aprendices


# Llena las listas solicitando datos al usuario hasta que se ingrese un nombre en blanco.
while len(aprendices)<max_aprendices: #len es una función incorporada que se utiliza para obtener la cantidad de elementos en una secuencia, como una lista, una cadena 
    nombre = input("Nombre del aprendiz: ")
    if nombre == "": 
        break
    edad = int(input("Edad del aprendiz: "))
    # Agrega el nombre a la lista de aprendices y la edad a la lista de edades.
    aprendices.append(nombre)
    edades.append(edad)

print("Lista de aprendices:", aprendices)
print("Lista de edades:", edades)

# Encuentra al aprendiz con la mayor edad.
mayor_edad = edades.index(max(edades)) # La función .index() de las listas busca un valor en la lista y devuelve su índice
print("El aprendiz con la mayor edad es:", aprendices[mayor_edad])
# Inserta el nombre de la instructora en la posición 1 de la lista de aprendices.
instructora = input("Nombre de la instructora: ")
aprendices.insert(1, instructora)

# Cuenta cuántos aprendices tienen 18 años.
contador_18 = 0
for edad in edades:
    if edad == 18:
        contador_18 += 1
print("El número de aprendices con 18 años es:", contador_18)

# Agrega un aprendiz ficticio llamado "x" al final de la lista de aprendices.

aprendices.append("eduardo")

# Borra el nombre de la instructora de la lista de aprendices.
aprendices.remove(instructora)
    
# Solicita un dato a buscar en la lista de aprendices y verifica si está presente.
dato_a_buscar = input("Dato a buscar en la lista de aprendices: ")
if dato_a_buscar in aprendices:
    print("El dato", dato_a_buscar, "se encuentra en la lista de aprendices.")
else:
    print("El dato", dato_a_buscar, "no se encuentra en la lista de aprendices.")

# Muestra los primeros 2 aprendices de la lista.
print("Los primeros 2 aprendices de la lista son:", aprendices[:2])

# Muestra los 2 últimos aprendices de la lista.
print("Los 2 últimos aprendices de la lista son:", aprendices[-2:])

# Muestra los elementos desde el 1 al 4 de la lista.
print("Los aprendices del elemento 1 al elemento 4 son:", aprendices[0:4])