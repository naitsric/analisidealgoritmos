import sys
import random
from time import clock, time
from datetime import timedelta
class Dados:
	def __init__(self):
		self.secreto = 0

		self.pointsP1 = 0
		self.pointsP2 = 0

		self.setMorePoints(1,100)
		self.setMorePoints(2,100)
		flag = True
		i = 0
		while flag:
			print "---------------------------------------------------------------------"
			#raw_input("Jugador 1: ")
			pt1 = self.jugar()
			print "Puntaje Player 1: " + str(pt1)
			tmFlag = True
			while tmFlag:
				#raw_input("Jugador 2: ")
				pt2 = self.jugar()
				if pt2!=pt1:
					tmFlag = False
			print "Puntaje Player 2: " + str(pt2)
			if pt1>pt2:
				self.setMorePoints(1,5)
				self.setMenPoints(2,5)
				print "Gana Jugador 1"
			if pt1<pt2:
				self.setMorePoints(2,5)
				self.setMenPoints(1,5)
				print "Gana Jugador 2"

			if self.pointsP1<= 0 or self.pointsP2 <= 0:
				print "---------------------------------------------------------------------"
				print "termino en " + str(i)
				print "---------------------------------------------------------------------"
				flag = False
			i = i + 1

			self.getPoints()
				
	def getPoints(self):
		print "P1: " + str(self.pointsP1)
		print "P2: " + str(self.pointsP2)

	def setMorePoints(self,op,pt):
		if op==1:
			self.pointsP1 = self.pointsP1+pt
		if op==2:
			self.pointsP2 = self.pointsP2+pt

	def setMenPoints(self,op,pt):
		if op==1:
			self.pointsP1 = self.pointsP1 - pt
		if op==2:
			self.pointsP2 = self.pointsP2 - pt

	def jugarDados(self):
		return random.randrange(1,6),random.randrange(1,6)

	def jugar(self):
		pt = self.jugarDados()
		return int(pt[0]) + int (pt[1])


Dados()