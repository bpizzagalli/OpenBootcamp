from pickle import *
class Vehic1e(object):
    marca=''
    puerta=0.0
def __init__(self, marca, puerta):
    self.marca=marca
    self.puerta=puerta
def getMarca(self):
    return self.marca
def getPuerta(self):
    return self.puerta

v1 = Vehicle('Bugatti', 10)
f=open('vehiculo', 'w+b')
dump(v1, f)
f.seek(6)
bugattiauto= load(f)
print(bugattiauto)
f.close()