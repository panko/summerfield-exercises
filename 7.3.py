# -*- coding: utf-8 -*-
# Gyakorlat 7.3.
# Definiáljon egy korTerulet(R) függvényt. A függvénynek egy kör területét kell visszaadni, aminek az 
# R sugarát argumentumként adjuk meg.
# Például a :print korTerulet(2.5) utasítás eredményének 19.635 ­nek kell lenni

import math

############fuggvenyek

def korTerulet(R):
	result=R**2*math.pi
	return result

###########torzs
sugar=float(input('Adja meg a kör sugarát: '))

print('A kör területe:',korTerulet(sugar))
