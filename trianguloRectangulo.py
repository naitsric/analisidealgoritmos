class TrianguloRec:
	def __init__(self,cat1,cat2,hipo):
		if (cat1^2 + cat2^2) == hipo^2:
			print "Si, es un Triangulo Rectangulo"
		else:
			print "No, no es un Triangulo Rectangulo"


cateto1 = raw_input("Digite el Primer Cateto: ")
cateto2 = raw_input("Digite el Segundo Cateto: ")
hipotenusa = raw_input("Digite la hipotenusa: ")

TrianguloRec(int(cateto1),int(cateto2),int(hipotenusa))