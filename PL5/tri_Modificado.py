contadortotal = 0       #INICIALIZA CONTADOR TOTAL
mes = 9     #MES DE NACIMIENTO (13/09/02)
umbral=mes+6        #UMBRAL ES MES + 6

for j in range(5,umbral+1,1):       #PARA UMBRAL VECES          (UNA EVALUACIÓN PARA CADA UMBRAL EN EL INTERVALO [5,MES+6]
    contador=0      #INICIALIZA CONTADOR DE UMBRAL
    print("Evaluando los valores en el umbral =",j)     #AVISO
    for i in range(1, j + 1, 1):       #PARA UMBRAL VECES
        if (((i ** 2 + i) / 2) < j):       #SI ES MENOR QUE UMBRAL
            print("Valor",i,"=",((i**2+i)/2),"<",j)        #OUTPUT
            contador = contador + 1     #ACTUALIZA CONTADOR
    print("Se han encontrado",contador,"números triangulares con el umbral =",j)        #OUTPUT
    contadortotal=contadortotal+contador        #ACTUALIZA CONTADOR TOTAL
    print()             #SEPARADOR

            #OUTPUT
print("Se han encontrado ", contadortotal, " números triangulares en los umbrales del intervalo [5,",umbral,"].",sep="")