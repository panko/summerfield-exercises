# -*- coding: utf-8 -*-
# Gyakorlat 6.10.
# Kérje   a   felhasználótól   a   nevét   és   a   nemét   (F   vagy   N)   .   Ezektől   az   adatoktól   függően   írassa   ki   a 
# felhasználó nevét és « Úr » ­at vagy « Asszony » ­t.

name=input('Adja meg a nevét: ')
sex=input('Adja meg a nemét (F vagy N): ')

if (sex == 'F') or (sex == 'f') or (sex == 'Férfi') or (sex == 'férfi'):
	print(name,'Úr')
if (sex == 'N') or (sex == 'n') or (sex == 'Nő') or (sex == 'nő'):
	print(name,'Asszony')
