class Vehiculo:

    color="black"
    ruedas=4
    puertas=2
class Coche(Vehiculo):
    velocidad=220
    cilindrada=1000
    
c = Coche()
print ("El coche posee una velocidad maxima de:", c.velocidad)
print ("Cilindrada del cochez", c.cilindrada)
print("Color del coche:", c.color)
print("Ruedas del cochez", c.ruedas)
print("Puertas del coche", c.puertas)