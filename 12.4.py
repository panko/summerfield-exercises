# -*- coding: utf-8 -*-
# Gyakorlat 12.4.
class Muhold:
	def __init__(self, nev, tomeg=100, sebesseg=0):
		self.nev=nev
		self.tomeg=tomeg
		self.sebesseg=sebesseg
	def impulsion(self,ero,idotartam):
		self.sebesseg+=ero*idotartam/self.tomeg
	def kiir_sebesseg(self):
		print('A',self.nev,'Muhold sebessege:',self.sebesseg,'m/s')
	def energia(self):
		nrg=self.tomeg*self.sebesseg**2/2
		print('A muhold kinetikus energiaja: {}'.format(nrg))

s1 = Muhold('Zoé', tomeg =250, sebesseg =10)
s1.impulsion(500, 15)
s1.kiir_sebesseg()

s1.energia()

s1.impulsion(500, 15)
s1.kiir_sebesseg()

s1.energia()



'''
A(z) Zoé műhold sebessége = 40 m/s.
200000
A(z) Zoé műhold sebessége = 70 m/s.
612500
'''
