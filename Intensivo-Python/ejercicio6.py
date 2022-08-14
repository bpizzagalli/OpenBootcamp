def password_converter(password):
    contador=0
    long=len(password)
    if long >=6 and long <=12:
        print("La contraseña es correcta")
        while len(password) <=32:
            
            password="a"+"1"+password+"b"+"2"
            print(password)
    
 

    else:
        print("La contraseña no es correcta")


password_converter('asdasddd')


