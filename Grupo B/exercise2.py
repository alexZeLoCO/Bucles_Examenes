#PROGRAM DEPENDS ON DECIDING WETHER 0 IS SEEN AS AND ODD NUMBER OR NOT.

sum=0       #TOTAL
for i in range (1,1000,1):      #FOR 1000 TIMES
    number=i        #NUMBER IS I
    digit=number%10     #PICK FIRST DIGIT OF THE NUMBER
    while (digit!=0 and digit%2!=0):        #WHILE DIGIT IS ODD AND NOT 0
        number=number//10       #REDUCE NUMBER
        digit=number%10     #PICK NEXT DIGIT

    if (digit==0):      #IF DIGIT IS 0 (EITHER ALREADY ODD OR ALL DIGITS GOT VERIFIED AS ODD)
        sum = sum + 1       #UPDATE SUM

    #OUTPUT
print("There are",sum,"numbers in the interval [1,1000] formed only by odd digits.")