# -*- coding: utf-8 -*-
# Gyakorlat 6.2.
# Írjon egy programot, ami kiszámolja a kerületét és a területét annak a háromszögnek, melynek 3 oldalát 
# a felhasználó adja meg. 
# (Ismétlés : egy háromszög területét a következő formula segítségével számoljuk ki :
# S = d⋅d −a⋅ d−b⋅d −c
# ahol d a kerület felét, a, b, c az oldalak hosszát jelöli).

import math

a=int(input('Adja meg a háromszög a oldalát: '))
b=int(input('Adja meg a háromszög b oldalát: '))
c=int(input('Adja meg a háromszög c oldalát: '))

kerulet=a+b+c
d=kerulet/2
terulet=math.sqrt(d*(d-a)*(d-b)*(d-c))
print(terulet)
print(kerulet)
