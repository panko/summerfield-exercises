# -*- coding: utf-8 -*-
# Gyakorlat 5.4.
# Írjon egy programot, ami a bankban elhelyezett 4,3 % ­os kamatozású tőke 20 év alatt 
# felhalmozódott évi kamatait számolja ki.

penz=int(input('Add meg a kezdőtőkét: '))
kamat=float(input('Add meg a kamatot: '))
futamt=int(input('Add meg a futamidőt években: '))

kamata=kamat/100+1		# atvaltja a kamatot hogy szorozhasson

for i in range(futamt):		# this is the core
	penz*=kamata
print(int(penz),'forint')
