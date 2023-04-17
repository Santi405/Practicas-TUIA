# 1a
def primeroA():
    base = int(input("Ingrese la base del rectangulo: "))
    altura = int(input("Ingrese la altura del rectangulo: "))

    area = base * altura
    perim = base * 2 + altura * 2
    print(f"El area del rectangulo es {area} y el perimetro es {perim}")

# 1b
def primeroB():
    var1 = int(input("Ingrese la variable entera 1: "))
    var2 = int(input("Ingrese la variable entera 2: "))
    var3 = int(input("Ingrese la variable entera 3: "))

    suma = var1 + var2
    prod = var2 * var3
    var3 = var1 * 3
    print(f"La suma de las dos primeras variables es: {suma} \nEl producto de las dos últimas es: {prod} \nEl nuevo valor de la variable 3 es: {var3}")


# 2a
def segundoA():
    num = input("Ingresar un valor entero (salir para terminar): ")

    if num == "salir":  
        quit()

    num = int(num)      
    if num < 0:
        print("El numero es negativo")
    elif num == 0:
        print("El numero es cero")
    else:
        print("El numero es positivo")

    if num % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

    segundoA()

#2b
def segundoB():
    num1 = int(input("Ingrese el primer valor: "))
    num2 = int(input("Ingrese el segundo valor: "))

    if num1 % num2 == 0:
        print("El primer valor es multiplo de M")
    else:
        print("El primer valor no es multiplo de M")


#3a
def terceroA():
    num = int(input("Ingrese el numero entero: "))
    if num == 1:
        print("El dia que le corresponde es lunes")
    elif num == 2:
        print("El dia que le corresponde es martes")
    elif num == 3:
        print("El dia que le corresponde es miercoles")
    elif num == 4:
        print("El dia que le corresponde es jueves")
    elif num == 5:
        print("El dia que le corresponde es viernes")
    elif num == 6:
        print("El dia que le corresponde es sabado")
    elif num == 7:
        print("El dia que le corresponde es domingo")
    else:
        print("Valor erroneo, debe ser entre 1 y 7, intente de nuevo")
        terceroA()
    terceroA()

#3b
def terceroB():
    num = input("Ingrese una letra")
    num = num.upper()

    if num == 'A' or num == 'E' or num == 'I' or num == 'O' or num == 'U':
        print("La letra es vocal")
    else:
        print("La letra no es vocal ")


#4a
def cuartoA():
    for x in range(10):
        print("Estoy probando")

#4b
def cuartoB():
    for x in range(10):
        print(f"Estoy probando {x+1}")

#4c
def cuartoC():
    for x in range(100):
        print(x+1)

#4d
def cuartoD():
    numList = []
    sumImp, cantImp, sumPares, cantPares = 0, 0, 0, 0
    
    for x in range(10):
        numList.append(int(input(f"Ingrese el numero {x+1}: ")))
    for x in numList:
        if x % 2 == 0:
            sumPares += x
            cantPares += 1
        else:
            sumImp += x
            cantImp += 1
    
    if cantPares == 0:
        cantPares = 1
    if cantImp == 0:
        cantImp = 1

    promPares = sumPares / cantPares
    promImp = sumImp / cantImp 

    print(f"El promedio de los pares es: {promPares}\nEl promedio de los impares es: {promImp}")

#4e
def cuartoE():
    numList = []
    cont = 0
    for x in range(100):
        if(x % 2 == 0 or x % 3 == 0):
            cont += 1
            numList.append(x)
    print(f"La cantidad de numeros es: {cont}\nLos numeros son: {numList}")

#4f
def cuartoF():
    numList = []
    cont = 0
    for x in range(100):
        if(x % 2 == 0 and x % 3 == 0):
            cont += 1
            numList.append(x)
    print(f"La cantidad de numeros es: {cont}\nLos numeros son: {numList}")

#4g
def cuartoG():
    numList = []
    max, min = 0, 10000000
    for x in range(10):
        numList.append(int(input(f"Ingrese el numero {x+1}: ")))
        if numList[x] > max:
            max = numList[x]
        elif x < min:
            min = x + 1
    
    print(f"El rango de los numeros ingresados es [{min},{max}]")

#4h
def cuartoH():
    numList = []
    sum = 0
    for x in range(10):
        numList.append(int(input(f"Ingrese el numero {x+1}: ")))
        sum += numList[x]
    prom = sum / 10

    print(f"El promedio de los numeros ingresados es: {prom}")

#4i
def cuartoI():
    notas = [4, 9, 1, 3, 3, 0, 6, 7, 2, 1, 10, 8, 3, 3, 3, 3, 10, 7, 5, 2, 4, 1, 9, 9, 8, 3, 8, 1, 6, 2, 9, 2, 6, 0, 7, 8, 8, 10, 9, 6, 5, 1, 7, 0, 7, 6, 2, 6, 9, 1, 1, 2, 4, 6, 6, 3, 0, 10, 10, 8, 7, 4, 2, 5, 9, 8, 0, 4, 8, 7, 0, 8, 1, 1, 5, 8, 2, 0, 3, 5, 9, 9, 2, 3, 6]
    suma, cont = 0, 0
    for x in notas:
        if x > 7:
            suma += x
            cont += 1

    prom = suma / cont
    print(f"El promedio de notas es de: {round(prom, 2)}")


#5a
def quintoA():
    while input("Quiere continuar? (S/N)") == "S":
        quintoA()

#5b
def quintoB():
    nota = ''
    suma, cont = 0, 0
    while True: # No muy fan de esto
        nota = input("Ingrese una nota (\'salir\' para terminar): ")
        if nota == "salir":
            break
        suma += int(nota)
        cont += 1
        
    prom = suma / cont

    print(f"El promedio de notas es: {prom}")

#5c
def quintoC():
    cont = 0
    while True:
        edad = input("Ingrese la edad del niño en años (\'salir\' para terminar): ")
        if edad == "salir":
            break
        peso = int(input("Ingrese su peso en kilogramos: "))
        estatura = int(input("Ingrese su estatura en centimetros: "))
        
        if int(edad) == 1:
            IMC = (peso * 10000) / (estatura ** 2)
            if(IMC < 12):
                cont += 1
    
    print(f"La cantidad de niños de un año con posible desnutrición es: {cont}")

#5d
def quintoD():
    while True:
        letra = input("Quiere continuar? (S/N): ")
        if letra == "S" or letra == "s":
            quintoD()
        elif letra == "N" or letra == "n":
            quit()
        else:
            print("Valor incorrecto, debe ser \'S\' o \'N\', intente de nuevo")
            quintoD()

#5e
def quintoE():
    suma, i = 0, 0
    while i < 100:
        print (i)
        suma += i
        i += 1
    print (f" Promedio : {suma / (i - 1)}")


