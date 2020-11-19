sexo=input("Introduzca el sexo (H/M): ")        #INPUT
while (sexo!="H" and sexo!="M"):     #SI NO ES VÁLIDO
    print ("Sexo inválido.")        #AVISO
    sexo = input("Introduzca el sexo (H/M): ")      #INPUT

edad=int(input("Introduzca la edad [5,120]: "))     #INPUT
while (edad<5 or edad>120):     #SI NO ES VÁLIDO
    print ("Edad inválida.")        #AVISO
    edad = int(input("Introduzca la edad [5,120]: "))       #INPUT

print("Una persona de sexo ",end="")        #OUTPUT (PARTE 1)
if (sexo=="H"):     #SI ES HOMBRE
    print("hombre y edad",edad,"se encuentra en la etapa de ",end="")       #OUTPUT (PARTE 2)
    if (edad<=13):              #CASO1
        print("Niñez")                          #OUTPUT (PARTE 3)
    elif (edad<=17):            #CASO2
        print("Adolescencia")                   #OUTPUT (PARTE 3)
    elif (edad<=35):            #CASO3
        print("Adultos jóvenes")                #OUTPUT (PARTE 3)
    elif (edad<=64):            #CASO4
        print("Adultos")                        #OUTPUT (PARTE 3)
    else:                       #CASO5
        print("Tercera edad")                   #OUTPUT (PARTE 3)

else:       #SI NO (ES MUJER)
    print("mujer y edad", edad, "se encuentra en la etapa de ", end="")     #OUTPUT (PARTE 2)
    if (edad<=13):              #CASO1
        print("Niñez")                          #OUTPUT (PARTE 3)
    elif (edad<=17):            #CASO2
        print("Adolescencia")                   #OUTPUT (PARTE 3)
    elif (edad<=35):            #CASO3
        print("Adultos jóvenes")                #OUTPUT (PARTE 3)
    elif (edad<=50):            #CASO4.1
        print("Pre-menopausia")                 #OUTPUT (PARTE 3)
        if (edad==50):          #EDAD=50 PERTENECE A AMBAS, POST Y PRE MENOPAUSIA
            print("Post-menopausia")            #OUTPUT (PARTE 3)
    elif (edad<=64):            #CASO4.2
        print("Post-menopausia")                #OUTPUT (PARTE 3)
    else:                       #CASO5
        print("Tercera edad")                   #OUTPUT (PARTE 3)