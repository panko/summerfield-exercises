#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# kész van de elég fapados


def indexMax(lista):
	a=0
	b=0
	c=0
	for i in lista:
		if i>a:
			a=i
			c=b
		b+=1

	return c 

sorozat=[5, 8, 2, 1, 9, 3, 6, 7]

print(indexMax(sorozat))
