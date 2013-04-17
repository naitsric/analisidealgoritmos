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
		# self.ordenamiento(self.coleccion)
		archi = open("Random.txt",'r')
		string = archi.read()
		self.coleccion = string.split(",")

		self.ordenamiento(self.coleccion)
		

	def ordenamiento(self,coleccion):
		nitera = 0
		d = timedelta(microseconds=-1)
		#archi = open("shellSort"+str(d.days)+" "+str(d.seconds)+" "+str(d.microseconds)+".txt",'a')
		#archi.write(str(coleccion))
		#archi.write("-------------------------------------------------------")
		start_time = time()
		incremento = len(coleccion)/2
		while incremento:
			for i in xrange(len(coleccion)):
				j = i
				temp = coleccion[i]
				while j>= incremento and coleccion[j-incremento]>temp:
					coleccion[j] = coleccion[j-incremento]
					j -= incremento
					nitera = nitera+1
				coleccion[j] = temp
			incremento = incremento/2 if incremento/2 else (0 if incremento==1 else 1)
		print time() - start_time, "seconds"
		print nitera, "iteraciones"
		#archi.write(str(coleccion))
		#archi.close()



#nDigitos = raw_input("Numero de Digitos: ")
#nPos = raw_input("Numero de Posiciones: ")
shellSort()