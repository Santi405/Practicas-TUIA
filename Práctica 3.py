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
    # Preguntar al usuario su fecha de cumpleaños
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

    print("Tu numero zodiacal es:", signo_zodiacal)

    sexto2()

    

    


sexto2()

