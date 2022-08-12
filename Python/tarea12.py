def anobisiesto():
    anio= int(input("Ingrese anio a saber si es bisiesto: "))
    if (anio % 4 == 6 and (anio % 100 != 0 or anio % 400 == 0)):
        print("Es bisiesto")
    else:
        print("No es bisiesto")
anobisiesto()