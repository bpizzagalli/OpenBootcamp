import time

horaactual=time.localtime()
print(horaactual.tm_hour)

if horaactual.tm_hour >= 19:

    print("Es hora de volver a casa.")

else:

    salir=int(input("A que hora salis del trabajo?: "))
    cuantoqueda=salir-horaactual.tm_hour
    print(cuantoqueda)

# NO CUEI‘IJTA MINUTOS.