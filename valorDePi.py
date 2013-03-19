import sys
"""importar la libreria sys"""
class Pi:
	"""definicion de la clase Pi"""
	def __init__(self,limite):
		"""iniciacion del constructor con parametro self y limite"""
		j = 0
		"""definicion de variable j"""
		i = float(3)
		"""definicion de variable i-trasformacion del numero 3 en float"""
		flag = False
		"""definicion de bandera es False"""
		pi = float(4)
		"""tomar num para convertirla en float definicion en Pi"""
		nround = self.Nround(limite)
		"""de la clase , tomar el metodo Nround"""
		print "It \t\t Num"
		"""Impresion con tabla con el It y Num"""
		while True:
			"""Mientras sea verdad se haga el ciclo"""
			#print "--------------------------------"
			if flag:
				"""si bandera"""
				pi = pi + (4/i)
				"""Pi toma el valor de la operacion indicada"""
				flag = False
				"""La bandera toma el valor False"""
			else:
				"""Sino"""
				pi = pi - (4/i)
				"""Pi toma el valor de la operacion indicada"""
				flag = True
				"""La bandera toma el valor True"""
			i = i+2
			"""El  contador aumenta en 2"""
			print str(j)+" \t\t "+str(pi)
			"""Impresion  de la variable j y pi tipo string"""
			#print round(pi,nround)
			#print limite
			if round(pi,nround) == limite:
				"""Si el valor dado por pi y nround es igual a limite"""
				print pi
				"""Imprime pi"""
				print "Iteraciones: " + str(j)
				"""imprime el numero de Iteraciones con j convertirla en string"""
				sys.exit();
				"""invoca la salida"""
			j = j + 1
			"""asigna al acumulador  uno mas"""
			#if j == 100:
			#	sys.exit();
	def Nround(self,limite):
		"""definicion del metodo Nround"""
		dec = str(limite).split(".")
		"""asignacion de un valor de la clase limite con el metodo split"""
		return len(dec[1])
		"""retorna el tamaño del valor"""
	def trunc(self,num,limite):
		"""definicion del constructor trunc"""
		dec = str(limite).split(".")
		"""asignacion de un valor de la clase limite con el metodo split"""
		strnum = str(num)
		"""asignacion del valor num en string a strnum"""
		return strnum[len(dec[0]),int(limite)+1]
		"""retorna strnum con el valor de la operacion"""



pi = raw_input("Digite el Limite para PI: ")
"""Impresion  de texto y toma del valor del limite Pi"""
Pi(float(pi))
"""conversion del Pi en float"""
