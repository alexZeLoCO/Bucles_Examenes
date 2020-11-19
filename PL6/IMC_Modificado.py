Contador=0

altura=float(input("Introduzca altura en metros: "))            #INPUT
while (altura<0.5 or altura>2.40):      #COMPROBACIÓN
    print ("La altura no es válida, debe ser mayor que 0.5 y menor que 2.40.")      #AVISO
    altura=float(input("Introduzca altura en metros: "))        #INPUT

peso=int(input("Introduzca peso en kilogramos: "))      #INPUT
while (peso<20 or peso>120):            #COMPROBACIÓN
    print ("El peso no es válido, debe ser mayor que 20 y menor que 120.")          #AVISO
    peso=int(input("Introduzca peso en kilogramos: "))      #INPUT

while (altura>0.5 and altura<2.40 and peso>20 and peso<120):

    IMC=float(peso/altura**2)       #CALCULO IMC
    if (IMC<25):        #SI ES MENOR QUE 25
        print("Riesgo promedio. Clasificación Normal.")     #OUTPUT
    elif (IMC<30):          #MENOR QUE 30
        print("Riesgo aumentado. Clasificación Sobrepeso.")     #OUTPUT
    elif (IMC<35):          #MENOR QUE 35
        print("MENSAJE ESPECIAL DE ADVERTENCIA.")       #OUTPUT
        print("Riesgo moderado. Clasificación Obesidad Grado I.")       #OUTPUT
    elif (IMC<40):          #MENOR QUE 40
        print("MENSAJE ESPECIAL DE ADVERTENCIA.")       #OUTPUT
        print("Riesgo severo. Clasificación Obesidad Grado II.")        #OUTPUT
    else:       #LO DEMÁS
        print("MENSAJE ESPECIAL DE ADVERTENCIA.")       #OUTPUT
        print("Riesgo muy severo. Clasificación Obesidad Grado III.")       #OUTPUT

    contador=contador+1     #ACTUALIZA CONTADOR

    altura = float(input("Introduzca altura en metros: "))  # INPUT
    while (altura < 0.5 or altura > 2.40):  # COMPROBACIÓN
        print("La altura no es válida, debe ser mayor que 0.5 y menor que 2.40.")  # AVISO
        altura = float(input("Introduzca altura en metros: "))  # INPUT
    peso = int(input("Introduzca peso en kilogramos: "))  # INPUT
    while (peso < 20 or peso > 120):  # COMPROBACIÓN
        print("El peso no es válido, debe ser mayor que 20 y menor que 120.")  # AVISO
        peso = int(input("Introduzca peso en kilogramos: "))  # INPUT

print("Se han calculado",contador,"IMCs.")      #OUTPUT