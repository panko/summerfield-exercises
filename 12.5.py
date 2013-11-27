# -*- coding: utf-8 -*-
# Gyakorlat 12.5.
# Definiáljon egy Kor() osztályt. Az osztályból létrehozott objektumok különböző méretű körök lesznek. 

import math

class Kor:
	def __init__(self,sugar):
		self.sugar=sugar
	def terulet(self):
		return self.sugar**2*math.pi

class Henger(Kor):
	def __init__(self,sugar,magassag):
		self.sugar=sugar
		self.magassag=magassag
	def terfogat(self):
		return (self.sugar**2*math.pi)*self.magassag
	def felszin(self):
		talaplap=self.sugar**2*math.pi			# meg kell szorozni még kettővel
		tpalast=(self.sugar*2*math.pi)*self.magassag
		felsz=2*talaplap+tpalast			#(self.sugar**2/math.pi)*2+self.magassag*(2*self.sugar/math.pi)
		return felsz


henger= Henger(5, 7)
print('Henger felszin:',henger.felszin())
print('Henger terfogat:',henger.terfogat())
kor=Kor(5)
print('Kör terulet:',kor.terulet())
