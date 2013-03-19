import sys							
"""importacion de la libreria"""
import random
"""importacion de la libreria random"""
from time import clock, time
"""importacion de la libreria time el tiempo del servidor de la maquina"""
from datetime import timedelta
"""de la libreria datetime la fecha actual """
class Adivina:
	"""definicion de la clase Adivina"""
	def __init__(self):
		"""constructor  de la clase Adivina"""
		self.secreto = 0
		"""invcacion de variable secreto"""
		flag = True
		"""bandera inicializada en true"""
		self.setSecreto()
		"""asignando otra variable dentro de la clase"""
		while flag:
			"""ciclo mientras que flag sea True"""
			num = raw_input("Ingrese el numero: ")
			"""se saca el letrero y se toma el valor y se asigana a num"""
			if int(num)>self.secreto:
				"""si entero es mayor que el valor de self secreto"""
				print "El numero es Menor"
				"""imprime en pantalla"""
			if int(num)<self.secreto:
				"""si entero es menor que el valor de self secreto"""
				print "El numero es Mayor"
				"""imprime en pantalla"""
			if int(num)==self.secreto:
				"""si entero es igual a self secreto"""
				flag = self.win()
				"""se va al metodo win"""

		print "Hasta Luego"
		"""imprime al terminar"""

	def setSecreto(self):
		"""definicion metodo setSecreto"""
		self.secreto = random.randrange(1,1000)
		"""definicion de setsecreto de la class random con extension del metodo randrange"""

	def win(self):
		print "Eres el Ganador"
		"""imprime letrero por Adivinar"""
		des = raw_input("Volver a Jugar (S=Si - N=No): ")
		"""Saca el letrero de Volver a Jugar y segun la desicion volver a la clase"""
		if des == "S":
			"""si des es igual a S """
			self.setSecreto()
			"""ingrese a metodo setSecreto"""
			return True
			"""retorna verdadero"""
		else:
			return False
			"""retorna verdadero"""

Adivina()