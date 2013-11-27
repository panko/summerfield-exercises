# -*- coding: utf-8 -*-
# Gyakorlat 5.13.
# Írjon egy programot, ami megkeresi egy adott lista legnagyobb elemét. Például, ha a  [32, 
# 5, 12, 8, 3, 75, 2, 15], listára alkalmaznánk, akkor a következőt kellene kiírnia :
# a lista legnagyobb elemének az értéke 75.

lista = [32, 5, 12, 8, 3, 75, 2, 15]
a=0
for i in range(len(lista)):
	if lista[i]>a:
		a=lista[i]
print('A lista legnagyobb eleme: {}.'.format(a))
