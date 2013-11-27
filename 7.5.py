#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# hasznalthatnám a max() fgvnyt is de az tul easy.

def maxim(n1,n2,n3):
	a=0
	lista=[n1,n2,n3]
	for i in lista:
		if i>a:
			a=i
	return a
print(maxim(423,3123,412))
