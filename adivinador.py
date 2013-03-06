import sys
import random
from time import clock, time
from datetime import timedelta
class Adivina:
	def __init__(self):
		self.secreto = 0
		flag = True
		self.setSecreto()
		while flag:
			num = raw_input("Ingrese el numero: ")
			if int(num)>self.secreto:
				print "El numero es Menor"
			if int(num)<self.secreto:
				print "El numero es Mayor"
			if int(num)==self.secreto:
				flag = self.win()

		print "Hasta Luego"

	def setSecreto(self):
		self.secreto = random.randrange(1,1000)

	def win(self):
		print "Eres el Ganador"
		des = raw_input("Volver a Jugar (S=Si - N=No): ")
		if des == "S":
			self.setSecreto()
			return True
		else:
			return False

Adivina()