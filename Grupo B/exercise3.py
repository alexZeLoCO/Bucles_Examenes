n=int(input("Input a positive number: "))       #INPUT
while (n<0):        #CHECK
    print ("Number is not positive.")           #WARNING
    n=int(input("Input a positive number: "))   #INPUT

for i in range (1,n+1,1):       #FOR N TIMES
    for j in range (1,n+1,1):       #FOR N TIMES
        if (i==j):      #ONLY WRITE IN DIAGONAL
            print("*",end="")       #OUTPUT
        else:       #IF NOT DIAGONAL
            print (" ",end="")      #OUTPUT
    print()     #GAP