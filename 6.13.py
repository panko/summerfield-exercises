# -*- coding: utf-8 -*-
# Gyakorlat 6.13.
# Konvertáljuk az iskolai N pontszámot, amit a felhasználó ad meg (például 85­ből 27) egy 
# standardizált jeggyé a következő feltételek szerint :
# Pont					Értékelés
# N >= 80 %				A
# 80 % > N >= 60 %		B
# 60 % > N >= 50 %		C
# 50 % > N >= 40 %		D
# N < 40 %				E
N=0

maxPont=float(input('Add meg a maximum pontszámot: '))
elertPont=float(input('Add meg az elért pontszámot: '))

if elertPont/maxPont*100>=80:
	N='A'
elif elertPont/maxPont*100>=60:
	N='B'
elif elertPont/maxPont*100>=40:
	N='C'
elif elertPont/maxPont*100>=20:
	N='D'
elif elertPont/maxPont*100>=0:
	N='E'
print('A te jegyed:', N)