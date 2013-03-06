import sys
from time import clock, time
from datetime import timedelta
class Factorial:
	def __init__(self,num):
		d = timedelta(microseconds=-1)
		archi=open(str(d.days)+" "+str(d.seconds)+" "+str(d.microseconds)+".txt",'a')
		start_time = time()
		fact = 1
		while num>0:
			fact = fact * num
			num = num -1
		archi.write(str(fact))
		archi.close()
		print time() - start_time, "seconds"
a= raw_input("Digite un numero: ")
Factorial(int(a))