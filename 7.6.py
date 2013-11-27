#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from turtle import *

#fuggvenys

def negyzet(meret, szin, szog):
	"meghatározott méretű és számú négyzetet rajzoló függvény"
	color(szin)
	c=0
	left(szog)
	while c<4:
		forward(meret)
		right(90)
		c+=1
def haromszog(meret, szin, szog):
	color(szin)
	left(szog)
	for i in range(0,3):
		forward(meret)
		right(120)
#magic

up()
goto(-350,50)	# itt kezdek

for i in range(1,6):
	down()
	negyzet(25*i, 'red', 0)
	up()
	forward(30*i)
	down()
	haromszog(25*i, 'blue', 0)
	up()
	forward(30*i)
a=input()
