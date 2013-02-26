import sys
class Restas:
	def __init__(self,divisor,dividendo):
		self.divisor = float(divisor)
		self.dividendo = float(dividendo)
	def division(self):
		self.getInfoDivi()
		bucles = 0
		dividendo = self.dividendo
		divisor = self.divisor
		sig = ""
		if divisor == 0:
			print "Imposible Dividir por 0"
			sys.exit()
		if divisor < 0:
			divisor = abs(divisor)
			sig = "-"

		if dividendo < divisor:
			print "El dividendo debe ser mayor al divisor"
			sys.exit()

		while (dividendo >= divisor):
			dividendo = dividendo - divisor
			bucles = bucles + 1

		print "Cosciente: ",sig,bucles
		print "Reciduo: ", dividendo
	def getInfoDivi(self):
		print str(self.dividendo) + " / " + str(self.divisor) + " = " + str(self.dividendo / self.divisor)

restar = Restas(-2,9)
restar.division()