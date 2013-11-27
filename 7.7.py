#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from turtle import *
from p76 import csillag5 

#magic

a=1
up()
goto(-350,50)	# itt kezdek
while a<=5:
	down()
	csillag5(30*a, 'blue', 0)
	up()
	forward(40*a)
	a+=1
while a>0:
	down()
	csillag5(30*a)
	up()
	forward(40*a)
	a-=1
a=input()
