# -*- coding: utf-8 -*-
# Gyakorlat 6.9.
# Határozzuk meg, hogy egy év szökőév vagy sem. (Az A év szökőév ha A osztható 4­gyel. Viszont nem 
# az, ha A többszöröse 100­nak, kivéve, ha A 400 ­nak többszöröse).

a=int(input('Adjon meg egy évet: '))
if (a%4==0) and ((a%100!=0) or (a%400==0)):
	print('ez egy szökőév')
else:
	print('ez nem egy szökőév')
