numero_inicial=int(input("Ingrese numero inicial "))
numero_final=int(input("Ingrese numero final "))
numeros_impares:[int]= []
for i in range(numero_inicial, numero_final+1):

    if(i%2 != 0):
        numeros_impares.append(i)

print("Lista numeros impares")
print(numeros_impares)