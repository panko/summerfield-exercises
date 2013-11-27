#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Gyakorlat 7.4.
# Definiáljon egy  dobozTerfogat(x1,x2,x3)  függvényt, ami egy parallelepipedon térfogatát adja vissza, 
# aminek a méreteit az x1, x2, x3 argumentumokban adjuk meg.
# Például   a :  print dobozTerfogat((5.2,  7.7,  3.3)  utasítás   végrehajtásakor   eredményül 
# 132.13 ­at kell kapnunk.

def dobozTerfogat(x1,x2,x3):
	return x1*x2*x3

print(dobozTerfogat(5.2,7.7,3.3))
