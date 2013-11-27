#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from turtle import *
from p76 import *

#fuggvenys
def csillag6(meret, szin='blue', szog=0):
	"hatágú csillag, 2 egymásra rajzolt egyenlooldalu 3szog"
	color(szin)
	left(szog)
	haromszog(meret, szin, 0)
	right(90)
	up()
	forward(meret/2)
	left(150)
	down()
	haromszog(meret, szin, 0)



#magic
a=0
up()
goto(-350,50)	# itt kezdek
down()
#innen rajzolok
while a<5:
	csillag6(30*a)
	negyzet(30*a)
	a+=1
a=input()
"EZ EGY KIBASZOT SZAR, NEM CSINÁLOM MEG"
