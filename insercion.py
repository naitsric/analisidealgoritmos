import sys
import random
from time import clock, time
from datetime import timedelta
class shellSort:
	def __init__(self):
		self.coleccion = []
		# min = ""
		# max = ""
		# for n in xrange(1,nDigitos):
		# 	min = "1"+min
		# 	max = "9"+max
		# for x in xrange(0,nPos):
		# 	self.coleccion.append(random.randrange(int(min),int(max)))
		# #print self.coleccion
		archi = open("Random.txt",'r')
		string = archi.read()
		self.coleccion = string.split(",")
		
		self.ordenamiento(self.coleccion)
		

	def ordenamiento(self,coleccion):
		nitera = 0
		d = timedelta(microseconds=-1)
		#archi = open("Insert "+str(d.days)+" "+str(d.seconds)+" "+str(d.microseconds)+".txt",'a')
		#archi.write(str(coleccion))
		#archi.write("-------------------------------------------------------")
		start_time = time()
		n = len(coleccion)
		for i in range(n):
			indice = coleccion[i]
			a = i-1
			while (a >= 0 and coleccion[a] > indice):
				coleccion[a+1] = coleccion[a]
				a = a-1
				nitera = nitera+1
			coleccion[a+1] = indice
		print time() - start_time, "seconds"
		print nitera, "iteraciones"
		#archi.write(str(coleccion))
		#archi.close()
		#print coleccion



#nDigitos = raw_input("Numero de Digitos: ")
#nPos = raw_input("Numero de Posiciones: ")
shellSort()