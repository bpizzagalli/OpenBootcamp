f=open('aescribir.txt', 'w')
lista=[
'estoy escribiendo\n', 'no se que poner\n', 'holaaaa\n', 'sfgdfdgs'
]
f.write1ines(lista)
f.write1ines('\nhola pone esto en el archivo a ver si funciona')
var='\nsi funciona'
f.writelines(var)
f.close()