age=int(input("Input age: "))           #AGE INPUT
income=float(input("Input income: "))     #INCOME INPUT
#TYPE FLOAT, INCOME MAY NOT BE A NATURAL NUMBER

if (age<30):        #IF AGE IS LOWER THAN 30
    if (income<12500):      #AND INCOME LOWER THAN 12500
        print((income * 2 / 100),"€, as the percentage to apply is 2%.")       #OUTPUT
    elif (income<25000):        #IF NOT, IF INCOME IS LOWER THAN 25000
        print((income * 4 / 100), "€, as the percentage to apply is 4%.")      #OUTPUT
    else:       #IF NONE OF THEM, THEN INCOME IS HIGHER THAN 25000
        print((income * 7 / 100), "€, as the percentage to apply is 7%.")      #OUTPUT
else:       #IF NOT, AGE IS HIGHER THAN 30
    if (income<12500):      #IF INCOME IS LOWER THAN 12500
        print((income * 5 / 100), "€, as the percentage to apply is 5%.")      #OUTPUT
    elif (income<25000):        #IF NOT, IF INCOME IS LOWER THAN 25000
        print((income * 9 / 100), "€, as the percentage to apply is 9%.")      #OUTPUT
    else:       #IF NONE OF THEM, THEN INCOME IS HIGHER THAN 25000
        print((income * 15 / 100), "€, as the percentage to apply is 15%.")    #OUTPUT