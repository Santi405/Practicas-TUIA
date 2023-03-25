#1
def primero():
    for x in range(1,21):
        print(x)

#2
def segundo():
    for x in range(5,51,5):
        print(x, end = ' ')

#3
def tercero():
    for x in range(-10,2):
        print(x, end = ' ')

#4
def cuarto():
    for x in [12 , 75 , 150 , 180 , 145 , 525 , 50]:
        if (x < 150) and (x % 5 == 0):
            print(x)

#5
def quinto():
    for x in [0,1,1,2,3,5,8,13,21,34]:
        print(x, end = ' ')

#6
def sexto():
    n = 1
    for x in range(1,6):
        n *= x
    print(n)

#7
    #a  En este programa se imprime el contenido de la lista 'lista', pero como esta está vacía, no imprime nada
    #b  En este programa se imprime la variable de iteración i, que va aumentando hasta llegar a 3 y terminar el for. Luego de que este termine, se imprime una última vez con el último valor.

#8

#a
def octavoA():
    for i in range(1,11):
        print(i ** 2, end = " ")

def octavoB():
    sumaHasta100 = 0
    for i in range(101):
        sumaHasta100 += i
    print(sumaHasta100)

def octavoC():
    sumaPares = 0
    for i in range(100):
        if i % 2 == 0:
            sumaPares += i
    print(sumaPares)     

def octavoD():
    sumaImpares = 0
    for i in range(100):
        if not i % 2 == 0:
            sumaImpares += i
    print(sumaImpares)    


#9 El problema con este programa es que nunca terminará, ya que la variable x no aumenta, por lo que su valor queda en 0 y siempre será menor a 5.

#10
def decimo():
    umbral = int(input("Ingrese el umbral de la suma: "))
    secuencia = input("Ingrese la secuencia de valores (sin corchete, separado por coma): ")
    suma = 0
    
    secuencia = list(secuencia.split(","))

    for i in secuencia:
        if (suma + int(i)) > umbral:
            break
        suma += int(i)
    print("La suma es: " + str(suma))

#11
def onceavo():

