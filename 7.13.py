#!/usr/bin/env python3
# -*- coding: utf-8 -*

def szavakSzama(mon):
	a=list(mon)
	b=0
	for i in a:
		if i == ' ':
			b+=1
	return b


print(szavakSzama("A kurva anyád."))
