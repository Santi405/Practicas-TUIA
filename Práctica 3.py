# 1
def primero():
    contra = input("Ingrese una contraseña: ")
    if len(contra) > 8:
        print("Es correcta.")
    else:
        print("Es incorrecta.")


# 2
def segundo():
    num = int(input("Ingrese un numero divisible por 4: "))
    if((num % 4) == 0):
        print("Es correcto.")
    else:
        print("Es incorrecto.")


#3
def tercero():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    num3 = int(input("Ingrese el tercer numero: "))

    if num1 > num2 and num1 > num3:
        print("El numero " + str(num1) + " es el mayor")
    elif num2 > num1 and num2 > num3:
        print("El numero " + str(num2) + " es el mayor")
    elif num3 > num2 and num3 > num1:
        print("El numero " + str(num3) + " es el mayor")

    # Si se buscara lo mismo pero con numero reales, cambiaria la función int por float.
    # Si se buscara lo mismo pero con caracteres o palabras, sacaría la función int.
    # Si se buscara el menor, cambiaría el > por <


#4
def cuarto():
    lado1 = int(input("Ingrese el largo del lado 1: "))
    lado2 = int(input("Ingrese el largo del lado 2: "))
    lado3 = int(input("Ingrese el largo del lado 3: "))

    if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
        print("Es equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Es isoceles")
    else:
        print("Es escaleno")


#5
def quinto():
    calif = input("Ingrese la calificación ")
    
    print("La calificación es: ", end='')
    match calif:
        case "I":
            print("5")
        case "A":
            print("6")
        case "B":
            print("7")
        case "M":
            print("8")
        case "D":
            print("9")
        case "E":
            print("10")
        case _:
            print("ERROR")


#6
def sexto():
    birthDate = input("Ingrese su fecha de nacimiento (MM/DD): ")

    if birthDate <= "1/20":
        print("Eres de capricornio ♑")
    elif birthDate >= "1/21" and birthDate <= "2/18":
        print("Eres de acuario ♒")
    elif birthDate >= "2/19" and birthDate <= "3/20":
        print("Eres de piscis ♓")
    elif birthDate >= "3/21" and birthDate <= "4/19":
        print("Eres de aries ♈")
    elif birthDate >= "4/20" and birthDate <= "5/20":
        print("Eres de tauro ♉")
    elif birthDate >= "5/21" and birthDate <= "6/20":
        print("Eres de géminis ♊")
    elif birthDate >= "6/21" and birthDate <= "7/22":
        print("Eres de cáncer ♋")
    elif birthDate >= "7/23" and birthDate <= "8/22":
        print("Eres de leo ♌")
    elif birthDate >= "8/23" and birthDate <= "9/22":
        print("Eres de virgo ♍")
    elif birthDate >= "9/23" and birthDate <= "10/22":
        print("Eres de libra ♎")
    elif birthDate >= "10/23" and birthDate <= "11/21":
        print("Eres de escorpio ♏")
    elif birthDate >= "11/22" and birthDate <= "12/21":
        print("Eres de sagitario ♐")
    else:
        print("ERROR: valor mal ingresado, intente de nuevo")
    sexto()


def sexto2():
    birthDate = input("Ingrese la fecha de su nacimiento: ")
    dia = int(birthDate[0:2])
    mes = int(birthDate[3:5])

    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        signo_zodiacal = "Acuario ♒"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        signo_zodiacal = "Piscis ♓"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        signo_zodiacal = "Aries ♈"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        signo_zodiacal = "Tauro ♉"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        signo_zodiacal = "Géminis ♊"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        signo_zodiacal = "Cáncer ♋"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        signo_zodiacal = "Leo ♌"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        signo_zodiacal = "Virgo ♍"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        signo_zodiacal = "Libra ♎"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        signo_zodiacal = "Escorpio ♏"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        signo_zodiacal = "Sagitario ♐"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        signo_zodiacal = "Capricornio ♑"
    else:
        print("Por favor, intente de nuevo")

    print(f"Tu numero zodiacal es: {signo_zodiacal}")
    sexto2()

sexto2()
#7

def septimo():
    zona = input("Ingrese la zona en la que estaba estacionado: ")
    hora = int(input("Ingrese cantidad de horas que estuvo estacionado: "))
    zona = zona.upper()

    if zona == "A":
        if hora == 1:
            print("El costo de estacionamiento es $57.")
        elif hora == 2:
            print("El costo de estacionamiento es $71,2.")
        elif hora == 3:
            print("El costo de estacionamiento es $85,5.")
    elif zona == "B":
        if hora == 1:
            print("El costo de estacionamiento es $47.")
        elif hora == 2:
            print("El costo de estacionamiento es $58,7.")
        elif hora == 3:
            print("El costo de estacionamiento es $70,5.")
    elif zona == "C":
        if hora == 1:
            print("El costo de estacionamiento es $37.")
        elif hora == 2:
            print("El costo de estacionamiento es $46,2.")
        elif hora == 3:
            print("El costo de estacionamiento es $55,5.")
    else:
        print("Error, intente de nuevo")
        septimo()

def octavo():
    item = input("Ingrese el item del producto: ")
    local = input("Ingrese la sede del local de ventas: ")
    item = item.capitalize()
    local = local.capitalize()

    if local == "Rosario":
        if item == "Zapatillas":
            print("El descuento es de 30% 👟")
        elif item == "Remeras":
            print("El descuento es de 20% 👕")
        elif item == "Pantalones":
            print("El descuento es de 10% 👖")
    elif local == "Funes":
        if item == "Zapatillas":
            print("El descuento es de 40% 👟")
        elif item == "Remeras":
            print("El descuento es de 30% 👕")
        elif item == "Pantalones":
            print("El descuento es de 5% 👖")
    elif local == "Roldán":
        if item == "Zapatillas":
            print("El descuento es de 25% 👟")
        elif item == "Remeras":
            print("El descuento es de 15% 👕")
        elif item == "Pantalones":
            print("El descuento es de 20% 👖")
    else: 
        print("ERROR, vuelva a intentarlo")
        octavo()


def noveno():
    item = input("Ingrese el item del producto: ")
    local = input("Ingrese la sede del local de ventas: ")
    dia = input("Ingrese el día de compra: ")
    item = item.capitalize()
    local = local.capitalize()
    dia = dia.capitalize()

    if dia == "Lunes":
        descuento = 10
    elif dia == "Miercoles" or dia == "Miercolés":
        descuento = 8
    elif dia == "Jueves":
        descuento = 5

    
    if local == "Rosario":
        if item == "Zapatillas":
            descuento += 30
            print("El descuento es de " + str(descuento)  +"% 👟")
        elif item == "Remeras":
            descuento += 20
            print("El descuento es de " + str(descuento) +"% 👕")
        elif item == "Pantalones":
            descuento += 10
            print("El descuento es de " + str(descuento) + "% 👖")
    elif local == "Funes":
        if item == "Zapatillas":
            descuento += 40
            print("El descuento es de " + str(descuento)  +"% 👟")
        elif item == "Remeras":
            descuento += 30
            print("El descuento es de " + str(descuento) +"% 👕")
        elif item == "Pantalones":
            descuento += 5
            print("El descuento es de " + str(descuento) + "% 👖")
    elif local == "Roldán" or local == "Roldan":
        if item == "Zapatillas":
            descuento += 25
            print("El descuento es de " + str(descuento)  +"% 👟")
        elif item == "Remeras":
            descuento += 15
            print("El descuento es de " + str(descuento) +"% 👕")
        elif item == "Pantalones":
            descuento += 5
            print("El descuento es de " + str(descuento) + "% 👖")
    else: 
        print("ERROR, vuelva a intentar")
        noveno()




        