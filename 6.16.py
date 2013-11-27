# -*- coding: utf-8 -*-
# Gyakorlat 6.16.
# Írjon egy scriptet, ami két 10000 kg tömegű test között ható gravitációs erő értékét íratja ki. 
# A  testek  közötti távolságok  5 cm  ­től (0,05 m) kezdődő  geometriai  sorozatot  alkotnak, 
# melynek kvóciense 2.
d = 0.5



while d < 10000:
	F = 6.67*(10**-11)*100000*100000/d**2
	print('d = {} : ez erős nagysága: {} N'.format(round(d, 1),F))
	d=d*2
	
