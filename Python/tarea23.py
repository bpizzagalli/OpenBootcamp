import sqlite3
conn = sqlite3.connect('miaplicacion.db')
c=conn.cursor()
def create_tab1e(nomtabl):
    c.execute(f'CREATE TABLE IF NOT EXISTS {nomtabl}(id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT)')

def data_entry(nomtabl, id, nom, ape):
    c.execute(f'INSERT INTO {nomtabl} VALUES({id}, "{nom}", "{ape}")')
    conn.commit()

def buscar_datos(nomtabl):
    rows=c.execute(f'SELECT * FROM {nomtabl}')

    for row in rows:
        print(row)

def buscar_por_nombre(nombre):
    busc=c.execute(f'SELECT * FROM alumnos NHERE nombre = "{nombre}"')

    for row in busc:
        print(row)

#data=busc.fetchone()
#print(f'{data}')
print("\nElija opcion: 1-crear tabla\nZ-insertar datos en tabla\n3-Buscar por nombre\n4-Mostrar datos de una tabla")
resp=-1

resp=int(input())
while resp != 0:
    if resp==1:
        nombretabla=input("Nombre de la tabla a crear: ")
        create_table(nombretabla)
    elif resp==2:
        tabl=input("Nom tabla a insertar: ")
        id=int(input("Id: "))
        nombre=input("Nombre: ")
        apellido=input("Apellid01 ")
        data_entry(tabl, id, nombre, apellido)
    elif resp==3:
        nombre=input("Nombre alumno a buscar (si hay dos con el mismo nombre imprime los dos): ")
        buscar_por_nombre(nombre)
    elif resp==4:
        tabl=input("Nom tabla a mostrar datos: ")
        buscar_datos(tabl)
    print("\nElija opcion: 1-crear tabla\n2-insertar datos en tabla\n3-Buscar por nombre\n4—Mostrar datos de una tabla")
    resp=int(input())