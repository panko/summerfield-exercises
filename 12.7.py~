# -*- coding: utf-8 -*-
# Gyakorlat 12.7.
'''
Definiáljon egy KartyaJatek()  osztályt, amiből olyan kártya objektumokat lehet létrehozni, amiknek a 
viselkedése   az   igazi   kártyákéra   hasonlít.   Az   osztálynak   legalább   a   következő   három   metódust   kell 
tartalmazni : 
­ constructor metódus : egy 52 elemű listát kell létrehozni és kitölteni, aminek az elemei az 52 kártya 
mindegyikének jellemzőit tartalmazó 2 elemű tuple­kből állnak. 
Mindegyik kártya esetén külön kell tárolni egy egész számot, ami megadja a kártya értékét (2, 3, 4, 5, 6, 
7, 8, 9, 10, 11, 12, 13, 14, az utolsó négy érték a junga, dáma, király és az ász) és egy másik egész 
számot, ami a kártya színét adja meg (azaz 3, 2, 1, 0 ­t a kőr, káró, a treff és a pik számára). 
Egy ilyen listában a (11,2) elem a tref jungát jelöli. A kész listának [(2, 0), (3,0), (3,0), (4,0),    ...  ... 
(12,3), (13,3), (14,3)] típusúnak kell lenni. 
­ kartya_neve() metódus : argumentumként megadva a leíró tuple­t, ez a metódus visszatérési értékként 
bármelyik kártyára megadja az azt azonosító karakterláncot. 
Például a : 
print jatek.kartya_neve((14, 3)) 
utasításnak :   pik ász ­t kell kiírni 
­ kever() metódus : összekeveri a kártyákat. 
A kártyákat tartalmazó lista elemeinek összekeverésére való, mindegy hány elemből áll a lista. 
­  huz()  metódus  :   amikor  ezt   a metódust   hívjuk,   akkor  egy   kártyát   húzunk.  A  színét  és  az  értékét 
tartalmazó tuple ­t adja meg visszatérési értékként a hívó programnak. Mindig  a lista első kártyáját 
húzzuk ki. Ha akkor hívjuk a metódust, amikor egyetlen kártya sem maradt a listában, akkor a speciális 
None objektumot kell megadnia visszatérési értékként. 
'''

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

jatek = KartyaJatek()
jatek.kever()
for n in range(53):
	c = jatek.huz() 
	if c == None:
		print('Vége !')
	else: 
		print(jatek.kartya_neve(c))



'''
kartya=KartyaJatek()
print(kartya.kartya_neve((14, 3)))
print(kartya.huz())
print(kartya.huz())
kartya.kever()
print(kartya.huz())
print(kartya.huz())
'''
