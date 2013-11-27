# -*- coding: utf-8 -*-
# Gyakorlat 6.12.
# Kérjük   meg   a   felhasználót,   hogy   írjon   be   egy   egész   számot.   Ezután   írassa   ki   ennek   a 
# számnak vagy a négyzetgyökét, vagy egy üzenetet,  ami jelzi, hogy ennek a számnak  a 
# négyzetgyökét nem lehet kiszámolni.

import math

numb=int(input('Adjon meg egy egész számot: '))
if numb >= 0:
	result=math.sqrt(numb)
	print(result)
else:
	print('Negatív számnak nem veheted a négyzetgyökét.')
