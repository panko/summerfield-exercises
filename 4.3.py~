# -*- coding: utf-8 -*-
# Gyakorlat 4.3
# Írjon egy programot, ami euróban kifejezett pézösszegeket kanadai dollárba vált át és az 
# eredményt egy táblázatba írja ki. A táblázatban a pézösszegek « geometriai haladvány » 
# szerint növekedjenek úgy, mint az alábbi példában : 
geo_hal=[1]
a=1
doll=1.65
for i in range(16384):
	a*=2
	geo_hal.append(a)
	if a == 16384:
		break
print(geo_hal)
for i in geo_hal:
	print('{} euro = {} dollar'.format(i,i*doll))
'''
1 euro = 1.65 dollar 
2 euro = 3.30 dollar 
4 euro = 6.60 dollar 
8 euro = 13.20 dollar 
stb. ( 16384 euronál kell megállni)
'''
