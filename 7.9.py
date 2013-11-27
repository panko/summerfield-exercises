#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#functions
def karakterSzam(ca, ch):
	'visszaadja a "ch" stringben előforduló "ca" karakterek számát.'
	eredmeny=0
	for i in ch:
		if i==ca:
			eredmeny+=1
	return eredmeny
#magic
a=karakterSzam('k', 'a budos nyomorek kurva anyukad.')
print(a)
