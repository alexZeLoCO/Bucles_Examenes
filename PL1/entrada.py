#INICIALIZAR VARIABLES
negativos=0
positivos=0
sumapares=0
sumaimpares=0

d=int(input("Introduzca fecha de nacimiento: "))        #SOLICITA D
print("Introduza números enteros en el rango [",-d,",",d,"]: ",sep="")

#EVALUACIÓN DE PRIMER DATO
n = int(input())  # SOLICITA DATO
if(n>-d and n<d):       #EVALUAR SÓLO SI ESTÁ COMPRENDIDO EN EL RANGO
    if (n<0):       #SI ES NEGATIVO
        negativos=negativos+1       #ACTUALIZAR NEGATIVOS
    elif (n>0):     #SI ES POSITIVO
        positivos=positivos+1       #ACTUALIZAR POSITIVOS

    #EL 0 NO LO CONTARÉ NI COMO POSITIVO NI COMO NEGATIVO, SI LO CONTASE COMO POSITIVO:
    #if (n<0):
    #   negativos=negativos+1
    #else:
    #   positivos=positivos+1

    if (n%2==0):        #SI ES DIVISIBLE ENTRE 2 (PAR)
        sumapares=sumapares+n       #ACTUALIZAR PARES
    else:               #SI NO (IMPAR)
        sumaimpares=sumaimpares+n   #ACTUALIZAR IMPARES

#EVALUACIÓN DEL RESTO DE DATOS
while (n>-d and n<d):       #MIENTRAS EL VALOR ESTÉ CONTENIDO EN EL RANGO
    n = int(input())  # SOLICITA DATO

    if(n>-d and n<d):       #EVALUAR SÓLO SI ESTÁ COMPRENDIDO EN EL RANGO
        if (n<0):       #SI ES NEGATIVO
            negativos=negativos+1       #ACTUALIZAR NEGATIVOS
        elif (n>0):     #SI ES POSITIVO
            positivos=positivos+1       #ACTUALIZAR POSITIVOS

        #EL 0 NO LO CONTARÉ NI COMO POSITIVO NI COMO NEGATIVO, SI LO CONTASE COMO POSITIVO:
        #if (n<0):
        #   negativos=negativos+1
        #else:
        #   positivos=positivos+1

        if (n%2==0):        #SI ES DIVISIBLE ENTRE 2 (PAR)
            sumapares=sumapares+n       #ACTUALIZAR PARES
        else:               #SI NO (IMPAR)
            sumaimpares=sumaimpares+n   #ACTUALIZAR IMPARES

#OUTPUT
print("La suma de valores pares introducidos es:",sumapares)
print("La suma de valores impares introducidos es:",sumaimpares)
print("El número de valores positovos introducidos es:",positivos)
print("El número de valores negativos introducidos es:",negativos)