#1a
def primeroA():
    list = [11 ,25 ,4 , 43 ,95]
    n, cont = 3, 0

    for i in list:
        if i == n:
            print(f"El indice en el que se encuentra el numero n es: {cont+1}")
            quit()
        cont += 1
    print("El numero no está en la lista")

#1b
def primeroB():
    list = [1 ,2 ,3 ,4 ,5, 10, 34]
    min, max = 100000, 0
    for i in list:
        if i > max:
            max = i
        if i < min:
            min = i
    print(f"El valor minimo es: {min}\nEl valor maximo es: {max}")

#1c
def primeroC():
    numList = [0, 1, 2, 3, 4]
    for i in range(len(numList)):
        numList[i] = numList[i]+1
    print(numList)

#1d
def primeroD():
    palabras = ["arbol" ,"barco" ,"artificial" ,"casa" ,"dado" ,"a" ]
    palA = []
    for i in palabras:
        if i.startswith('a') or i.startswith('A'):
            palA.append(i)
    print(palA)

#1e
def primeroE():
    numList = [0 ,1 ,2 ,3 ,4 ,5]
    sumPar, multImp = 0, 1

    for i in range(len(numList)):
        print(i)
        if i % 2 == 0:
            sumPar += numList[i]
        else:
            multImp *= numList[i]
    print(f"La suma de los indice par es: {sumPar} \nEl producto de los indice impar es: {multImp}")

#1f
def primeroF():
    numList = [0 ,1 ,2 ,3 ,4 ,5]
    print(numList[::-1])


#2a
def segundoA():
    numList = [0 ,1 ,2 ,3 ,4 ,5]
    for i in range(len(numList)):
        if i != 0:
            numList[i] += numList[i-1]
    print(numList)


#3a
def terceroA():
    numList = [0 ,1 ,2 ,3 ,2 ,4 ,5]
    newList = []
    for i in range(len(numList)):
        for j in numList[i+1:]:
            if j == numList[i]:
                newList.append(i)
                newList.append(j)
    print(newList)

#4a
def cuartoA():
    lst = [0,1]

    n = int(input("Ingrese la cantidad de numeros deseados: "))
    for i in range(n):
        newVal = lst[-2] + lst[-1]
        lst.append(newVal)
    print(lst)

#5a
def quintoA():
    datos_personales = []
    datos_personales.append(input("Ingrese el nombre del alumno: "))
    datos_personales.append(input("Ingrese el apellido del alumno: "))
    datos_personales.append(input("Ingrese la localidad del alumno: "))
    datos_personales.append(input("Ingrese la edad del alumno: "))
    datos_personales.append(input("Ingrese el DNI del alumno: "))
    datos_personales.append(input("Ingrese la carrera universitaria del alumno: "))
    datos_personales.append(input("Ingrese el año de inicio de carrera del alumno: "))

    print(datos_personales)

#5b
def quintoB():
    lista = [ ' María ' , ' Gonzalez ' , ' Chascom ú s ' , 24 , 50708934 ,' Ing . civil ' , 2022]
    años_cursando = 2023 - int(lista[-1])
    print(f"Le alumnx se llama {lista[0] + lista[1]}, lleva estudiando {años_cursando} año/s")

#5c
def quintoC():
    datos_personales = []                       # Inicio de listas
    baseDeDatos = []
    while True:
        datos_personales.append(input("Ingrese el nombre del alumno (1 para salir): "))
        if datos_personales[0] == "1":
            break
        datos_personales.append(input("Ingrese el apellido del alumno: "))
        datos_personales.append(input("Ingrese la localidad del alumno: "))
        datos_personales.append(input("Ingrese la edad del alumno: "))
        datos_personales.append(input("Ingrese el DNI del alumno: "))
        datos_personales.append(input("Ingrese la carrera universitaria del alumno: "))
        datos_personales.append(input("Ingrese el año de inicio de carrera del alumno: "))

        baseDeDatos.append(datos_personales)    # Se añade el alumno
        datos_personales = []                   # Reinicio de lista
    print(baseDeDatos)

def quintoD():
    lista = [['Santino', 'Zanin', 'Rosario', '19', '45412822', 'ISI', '2023'], ['Martín Pérez', 'Disalvo', 'La Plata', '31', '37485215', 'Nada', '2012']]
    for i in range(len(lista)):
        lista[i][5] = 'TUIA'
    print(lista)

quintoD()