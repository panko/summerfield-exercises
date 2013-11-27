# -*- coding: utf-8 -*-
# Gyakorlat 6.14.
# Legyen a következő felsorolás egy lista :
# ['Jean­Michel', 'Marc', 'Vanessa', 'Anne', Maximilien', 'Alexandre­Benoît', 'Louise']
# Írjon egy scriptet, ami kiírja ezen nevek mindegyikét és a karaktereik számát.

lista=['Jean­Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre­Benoît', 'Louise']
for i in lista:
	print(i, end=' ')
	print(len(i))