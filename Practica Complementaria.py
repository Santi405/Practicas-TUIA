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