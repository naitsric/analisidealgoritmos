import sys
import random
from time import clock, time
from datetime import timedelta
class generarPlano:
	def __init__(self,nDigitos,nPos):
		self.coleccion = []
		min = ""
		max = ""
		archi = open("Random.txt",'a')
		for n in xrange(1,nDigitos):
			min = "1"+min
			max = "9"+max
		for x in xrange(0,nPos):
			#archi.write(random.randrange(int(min),int(max)))
			#archi.write(",")
			#archi.write(str(random.randrange(int(min),int(max))))
			#archi.write(",")
			self.coleccion.append(str(random.randrange(int(min),int(max))))
		#self.ordenamiento(self.coleccion)
		archi.write(",".join(self.coleccion))
		#with open(fname) as f:
    	#content = f.readlines()
		archi.close()

print "Generando el Ramdom"
nDigitos = raw_input("Numero de Digitos: ")
nPos = raw_input("Numero de Posiciones: ")
generarPlano(int(nDigitos),int(nPos))