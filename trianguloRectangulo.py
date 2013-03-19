class TrianguloRec:
	"""Definicion de la clase TrianguloRec"""
	def __init__(self,cat1,cat2,hipo):
		"""Inicializando el constructor"""
		if (cat1^2 + cat2^2) == hipo^2:
			"""Condicion si la operacion se cumple"""
			print "Si, es un Triangulo Rectangulo"
			"""Imprime en pantalla"""
		else:
			print "No, no es un Triangulo Rectangulo"
			"""Imprime en pantalla"""

Lista = []
"""Definicion de Lista como array"""
Lista.append(raw_input("Digite el Primer Lado: "))
"""Toma de dato para el primer cateto"""
Lista.append(raw_input("Digite el Segundo Lado: "))
"""Toma de dato para el Segundo cateto"""
Lista.append(raw_input("Digite el Tercer Lado: "))
"""Toma de dato para la hipotenusa"""

Lista2 = sorted(Lista)

TrianguloRec(int(Lista2[0]),int(Lista2[1]),int(Lista2[2]))
"""Enviando a la clase los valores"""