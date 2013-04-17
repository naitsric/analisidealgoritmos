import sys
import random
from time import clock, time
from datetime import timedelta
class shellSort:
	def __init__(self,nDigitos,nPos):
		self.coleccion = []
		# min = ""
		# max = ""
		# for n in xrange(1,nDigitos):
		# 	min = "1"+min
		# 	max = "9"+max
		# for x in xrange(0,nPos):
		# 	self.coleccion.append(random.randrange(int(min),int(max)))
		archi = open("Random.txt",'r')
		string = archi.read()
		self.coleccion = string.split(",")
		print self.coleccion
		self.ordenamiento(self.coleccion)
		print self.coleccion

	def ordenamiento(self,coleccion):
		print coleccion
		nitera = 0
		d = timedelta(microseconds=-1)
		archi = open("Select "+str(d.days)+" "+str(d.seconds)+" "+str(d.microseconds)+".txt",'a')
		archi.write(str(coleccion))
		#print coleccion
		archi.write("-------------------------------------------------------")
		start_time = time()
		n = len(coleccion)
		for i in range(1,n-1,2):
			#print "i: "+str(i)
			#i = i+1
			print "i: ->"+str(i)
			k = i
			t = coleccion[i]
			
			for j in range(i,n,2):
				#print "j: "+str(j)
				#j = j+1
				print "j: ->"+str(j)
				nitera = nitera+1
				if coleccion[j] < t:
					k = j
					t = coleccion[j]
			coleccion[k] = coleccion[i]
			coleccion[i] = t
		print time() - start_time, "seconds"
		print nitera, "iteraciones"
		archi.write(str(coleccion))
		archi.close()
		print coleccion



nDigitos = raw_input("Numero de Digitos: ")
nPos = raw_input("Numero de Posiciones: ")
shellSort(int(nDigitos),int(nPos))