semifact=1

        #GUÍA USUARIO
print("En un intervalo del tipo [a,b] en el que a>=0, b>=0, b>=a y b<10...")
a=int(input("Defina a: "))     #INPUT
b=int(input("Defina b: "))      #INPUT
while (a<0 or a>=10):        #COMPROBACIÓN A
    print("Número introducido no válido, a>=0, b>=0, b>=a y b<10: ")      #AVISO
    n=int(input("Defina a: "))     #INPUT

while (b<0 or b<a or b>=10):        #COMPROBACIÓN B
    print("Número introducido no válido, a>=0, b>=0, b>=a y b<10: ")      #AVISO
    n=int(input("Defina b: "))     #INPUT

for i in range (b,a-1 or a,-2):       #PARA N/2 VECES, SALTANDO DE 2 EN 2 HASTA 1 Ó 2 (INCLUIDOS)
    semifact=semifact*i     #ACTUALIZAR SEMIFACTORIA
    if(i-2==-1 or i-2==0):      #SI ES LA ÚLTIMA ITERACIÓN
        print("La semifactorial de ", a, " hasta ",b," es ", semifact, ".", sep="")  # OUTPUT

#FUERA DEL FOR, SEMIFACT ES 0, POR LO QUE OUTPUT DEBE ESTAR DENTRO DEL FOR - O QUE EL FOR SEA UNA VARIABLE GLOBAL -
