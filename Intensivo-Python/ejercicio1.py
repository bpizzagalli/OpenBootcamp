import os
descargas = os.listdir("D:\Descargas")
#Puse la ubicacion de mi carpeta de Descargas

for i in descargas:
    
    if os.path.isfile("D:\Descargas\\"+i) == True:
        print (f'{i} es un archivo')    
    else:
        print (f'{i} no es un archivo')
    tamanio= os.path.getsize("D:\Descargas\\"+i)
    print(f'Su tamanio es: {tamanio} bytes')


