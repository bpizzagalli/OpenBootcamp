listapaises=[]
rta=input('Queres agregar mas paises? S/N ')
while rta == 's' or rta == 'S':
    pais=input('Ingrese nombre del pais a agregar: ')
    listapaises.append(pais)
    print (listapaises)
    rta=input('Queres agregar mas paises? S/N: ')

listapaises=set(listapaises)
listapaises=sorted(listapaises)
print (listapaises)