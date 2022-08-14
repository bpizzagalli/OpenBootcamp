
print("1-Agregar contacto\n2-Buscar contacto por nombre\n0-Salir")
resp = -1

resp=int(input())
dictionary={}

while resp != 0:
    if resp==1:
        nombre=input("Ingrese nombre: ")
        telefono=int(input("Ingrese telefono: "))
        dictionary.update({nombre:telefono})
        

    elif resp == 2:
        nombre=input("Ingrese nombre: ")
        if nombre in dictionary:
            print(f'El telefono de {nombre} es:', dictionary.get(nombre))
        else:
            print("No existe")
    
    print("1-Agregar contacto\n2-Buscar contacto por nombre\n0-Salir")
    resp=int(input())
        




