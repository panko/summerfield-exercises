# -*- coding: utf-8 -*-
# Gyakorlat 6.4.
# Írjon egy programot, ami értékeket tesz egy listába. Ennek a programnak ciklusban kell működni úgy, 
# hogy mindaddig kéri az értékeket, amíg a felhasználótól úgy nem dönt, hogy befejezésként   <Entert> 
# üt. A program a lista kiírásával fejeződik be.

lista=[]
while 1 > 0:
	temp=input('Írjon be egy értéket : ')
	if temp == '':
		break
	else:
		lista.append(temp)
print(lista)
