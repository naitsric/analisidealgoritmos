import sys
"""importacion de la libreria sys"""
import random
"""importacion de la libreria random"""
from time import clock, time
"""importacion de la libreria clock de time"""
from datetime import timedelta
"""importacion de la libreria datetime de timedelta"""
class Dados:
	"""definicion de la clase Dados"""
	def __init__(self):
		"""inicializando el constructor"""
		self.secreto = 0
		"""Asignando valor a secreto"""

		self.pointsP1 = 0
		"""Asignando valor a pointsP1"""
		self.pointsP2 = 0
		"""Asignando valor a pointsP2"""
		self.setMorePoints(1,100)

		self.setMorePoints(2,100)
		flag = True
		"""La bandera Asignando verdadero"""
		i = 0
		"""Asignando valor 0 a i"""
		while flag:
			"""Mientras la bandera siga True realizar"""
			print "---------------------------------------------------------------------"
			pt1 = self.jugar()
			"""LLamar el metodo jugar"""
			print "Puntaje Player 1: " + str(pt1)
			"""Imprime el Puntaje del Jugador"""
			tmFlag = True
			"""La bandera Asignando verdadero"""
			while tmFlag:
				"""Mientras se cumpla la condición"""
				#raw_input("Jugador 2: ")
				pt2 = self.jugar()
				"""LLamar el metodo jugar"""
				if pt2!=pt1:
					"""si pt2 es diferente de pt1"""
					tmFlag = False
					"""La bandera es False"""
			print "Puntaje Player 2: " + str(pt2)
			"""Imprime el Puntaje del Jugador"""
			if pt1>pt2:
				"""Si el valor de pt1 es mayor que pt2"""
				self.setMorePoints(1,5)
				"""Envia valores al metodo setMorePoints"""
				self.setMenPoints(2,5)
				"""Envia valores al metodo setMenPoints"""
				print "Gana Jugador 1"
				"""Imprime letrero en pantalla"""
			if pt1<pt2:
				"""Si el valor de pt2 es mayor que pt1"""
				self.setMorePoints(2,5)
				"""Envia valores al metodo setMorePoints"""
				self.setMenPoints(1,5)
				"""Envia valores al metodo setMenPoints"""
				print "Gana Jugador 2"
				"""Imprime letrero en pantalla"""

			if self.pointsP1<= 0 or self.pointsP2 <= 0:
				"""Si los puntos son menores a 0, se termino el juego"""
				print "---------------------------------------------------------------------"
				print "termino en " + str(i)
				"""Imprime valores termino"""
				print "---------------------------------------------------------------------"
				flag = False
			i = i + 1
			"""Contador suma 1"""

			self.getPoints()
			"""inicializando el metodo getPoints"""
				
	def getPoints(self):
		"""definicion del metodo"""
		print "P1: " + str(self.pointsP1)
		"""Asignando el valor de P1"""
		print "P2: " + str(self.pointsP2)
		"""Asignando el valor de P2"""

	def setMorePoints(self,op,pt):
		"""definicion del metodo"""
		if op==1:
			"""Si el valor recibido es = a 1"""
			self.pointsP1 = self.pointsP1+pt
			"""Asignando un valor sumandole puntos"""
		if op==2:
			"""Si el valor recibido es = a 2"""
			self.pointsP2 = self.pointsP2+pt
			"""Asignando un valor sumandole puntos"""

	def setMenPoints(self,op,pt):
		if op==1:
			"""Si el valor recibido es = a 1"""
			self.pointsP1 = self.pointsP1 - pt
			"""Asignando un valor sumandole puntos"""
		if op==2:
			"""Si el valor recibido es = a 2"""
			self.pointsP2 = self.pointsP2 - pt
			"""Asignando un valor sumandole puntos"""

	def jugarDados(self):
		"""definicion del metodo"""
		return random.randrange(1,6),random.randrange(1,6)
		"""Retornando el valor con el metodo random.randrange"""

	def jugar(self):
		"""definicion del metodo"""
		pt = self.jugarDados()
		"""Asignando un valor a pt con el metodo jugarDados"""
		return int(pt[0]) + int (pt[1])
		"""Retornando los valores"""


Dados()