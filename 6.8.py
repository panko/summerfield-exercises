# -*- coding: utf-8 -*-
# Gyakorlat 6.8.
# Írjon   egy   programot,   ami   adott   a  és  b   egész  korlátok   esetén   összeadja  a  3  és  5   korlátok   közé   eső többszöröseit.
# Vegyük például az a=0, b=32 ­t →  az eredménynek 0 +15 +30 = 45 ­nek kell lenni.
# Módosítsa úgy a programot, hogy az adja össze a 3­nak  vagy  az 5­nek az a és b határok közé eső 
# többszöröseit. A 0 és 32 határokkal az eredménynek : 0 + 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20 + 21 +  
# 24 + 25 + 27 + 30 = 225 ­nek kell lenni.

a=int(input('Add meg az alsókorlátot: '))
b=int(input('Add meg az felsőkorlátot: '))

c=0

for i in range(a,b+1):
	if (i%3==0) or (i%5==0):
		c+=i
print(c)
