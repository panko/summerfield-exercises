# -*- coding: utf-8 -*-
# Gyakorlat 12.8.


from random import shuffle

class KartyaJatek:
	szinek=['kőr', 'káró', 'treff', 'pikk']
	ertekek=[None, None, 'kettő','három', 'négy', 'öt', 'hat', 'hét', 'nyolc', 'kilenc', 'tíz', 'bubi', 'dáma', 'király', 'ász']
	def __init__(self):
		self.kartyak=[]
		for szin in range(4):	
			for ertek in range(2,15):
				self.kartyak.append((ertek,szin))
	def kartya_neve(self,tapl):
		for i in self.kartyak:
			if i == tapl:
				self.ertek=self.ertekek[i[0]]
				self.szin=self.szinek[i[1]]
		return '{} {}'.format(self.szin,self.ertek)
	def kever(self):
		shuffle(self.kartyak)
	def huz(self):
		try:
			a=self.kartyak[0]
			del self.kartyak[0]
		except IndexError:
			return None
		
		self.ertek=self.ertekek[a[0]]
		self.szin=self.szinek[a[1]]
		return '{} {}'.format(self.szin,self.ertek)



playera=KartyaJatek()
playerb=KartyaJatek()
playera.kever()
playerb.kever()
aa=0
bb=0
a=0
b=0
for i in range(53):
	try:
		aa+=playera.kartyak[0][0]
	except IndexError:
		break
	playera.huz()
	try:
		bb+=playerb.kartyak[0][0]
	except IndexError:
		break
	playerb.huz()
	
	if aa>bb:
		a+=1
	else:
		b+=1
if a>b:
	print('Nyert az A jatkos.')
else:
	print('Nyert a B jatekos.')
