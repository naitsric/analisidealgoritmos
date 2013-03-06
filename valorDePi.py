import sys
class Pi:
	def __init__(self,limite):
		j = 0
		i = float(3)
		flag = False
		pi = float(4)
		nround = self.Nround(limite)
		while True:
			#print "--------------------------------"
			if flag:
				pi = pi + (4/i)
				flag = False
			else:
				pi = pi - (4/i)
				flag = True
			i = i+2
			#print round(pi,nround)
			#print limite
			if round(pi,nround) == limite:
				print pi
				print "Iteraciones: " + str(j)
				sys.exit();
			j = j + 1
			#if j == 100:
			#	sys.exit();
	def Nround(self,limite):
		dec = str(limite).split(".")
		return len(dec[1])
	def trunc(self,num,limite):
		dec = str(limite).split(".")
		strnum = str(num)
		return strnum[len(dec[0]),int(limite)+1]



pi = raw_input("Digite el Limite para PI: ")
Pi(float(pi))
