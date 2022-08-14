
def primos(num):
    lista=[]
    cont=0
    for i in range(2, num+1):
        primo=True
        for j in range(2,i):
            if i==j:
                continue
            elif i%j==0:
                primo=False
            else:
                continue
        if primo == True:
            lista.append(i)
            cont+=1
    print(lista)
    print(f'Hay {cont} numeros primos')


num=int(input("Ingrese hasta que numero va a iterar: "))
primos(num)