# -*- coding: utf-8 -*-
# Gyakorlat 4.8.
# Írjon egy programot, ami kiszámolja 13­as szorzótábla első 50 tagját, de csak azokat írja ki, 
# melyek 7­nek többszörösei.

for i in range(1,51):
	if (13*i)%7==0:
		print(i*13)
