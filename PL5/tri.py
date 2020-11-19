contador=0      #INICIALIZA CONTADOR

umbral=int(input("Introduzca un número entero umbral (>1): "))      #INPUT
while (umbral<=1):      #DEBE SER MAYOR IGUAL QUE 1
    print("Valor umbral no válido. Debe ser >1.")          #AVISO
    umbral = int(input("Introduzca un número entero umbral (>1): "))        #INPUT

for i in range (1,umbral+1,1):      #PARA UMBRAL VECES
    if (((i**2+i)/2)<umbral):       #SI I ES MENOR QUE UMBRAL
        print("Valor",i,"=",((i**2+i)/2),"<",umbral)        #OUTPUT
        contador=contador+1     #ACTUALIZA CONTADOR

        #OUTPUT
print("Se han encontrado",contador,"números triangulares.")