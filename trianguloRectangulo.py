class TrianguloRec:
	def __init__(self,cat1,cat2,hipo):
		if (cat1^2 + cat2^2) == hipo^2:
			print "Si, es un Triangulo Rectangulo"
		else:
			print "No, no es un Triangulo Rectangulo"

Lista = []
Lista.append(raw_input("Digite el Primer Lado: "))
Lista.append(raw_input("Digite el Segundo Lado: "))
Lista.append(raw_input("Digite el Tercer Lado: "))

Lista2 = sorted(Lista)

TrianguloRec(int(Lista2[0]),int(Lista2[1]),int(Lista2[2]))