#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from turtle import *

#fuggvenys

def csillag6(meret, szin='blue', szog=0):
	"hatágú csillag, 2 egymásra rajzolt egyenlooldalu 3szog"
	color(szin)
	left(szog)
	for i in range(0,3):	#felso haromszog
		forward(meret)	
		right(120)
	right(90)
	up()
	forward(meret/2)
	left(150)
	down()
	for i in range(0,3):
		forward(meret)
		right(120)

def csillag5(meret, szin='blue', szog=0):
	"meghatarozott meretu 5szogu csillagot rajzol."
	color(szin)
	left(szog)
	for i in range(0,5):
		forward(meret)
		right(144)

def negyzet(meret=30, szin='red', szog=0):
	"meghatározott méretű és számú négyzetet rajzoló függvény"
	color(szin)
	c=0
	left(szog)
	while c<4:
		forward(meret)
		right(90)
		c+=1
def haromszog(meret=30, szin='red', szog=0):
	color(szin)
	left(szog)
	for i in range(0,3):
		forward(meret)
		right(120)
#magic

if __name__ == "__main__":
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
