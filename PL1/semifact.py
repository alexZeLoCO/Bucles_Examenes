semifact=1

n=int(input("Introduzca un natural: "))     #INPUT
while (n<0):        #COMPROBACIÓN
    print("Número introducido no válido, introduzca un natural: ")      #AVISO
    n=int(input("Introduzca un natural: "))     #INPUT

for i in range (n,-1 or 0,-2):       #PARA N/2 VECES, SALTANDO DE 2 EN 2 HASTA 1 Ó 2 (INCLUIDOS)
    semifact=semifact*i     #ACTUALIZAR SEMIFACTORIA
    if(i-2==-1 or i-2==0):      #SI ES LA ÚLTIMA ITERACIÓN
        print("La semifactorial de ", n, " es ", semifact, ".", sep="")  # OUTPUT

#FUERA DEL FOR, SEMIFACT ES 0, POR LO QUE OUTPUT DEBE ESTAR DENTRO DEL FOR - O QUE EL FOR SEA UNA VARIABLE GLOBAL -
