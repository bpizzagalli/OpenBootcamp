def numprimo(num):
    for i in range(2,num):
        if num%i ==0:
            print("No es primo")
            break
        else:
            print("Es primo")
            break
numprimo(5)