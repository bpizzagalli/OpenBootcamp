class Alumno:
    nombre=input("Ingrese nombre: ")
    nota=int(input("Nota: "))

def imprimirDatos(se1f):
    print("Nombre:", Alumno.nombre)
    print("Nota:", Alumno.nota)
def aprobo(se1f):
    if Alumno.nota > 7:
        print("El alumno ", Alumno.nombre, "aprobo con nota: ", Alumno.nota)
    else:
        print("El alumno ", Alumno.nombre, "no aprobo con nota: ", Alumno.nota)

a = Alumno()
a.imprimirDatos()
a.aprobo()