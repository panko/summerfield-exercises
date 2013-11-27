# -*- coding: utf-8 -*-
# Gyakorlat 6.3.
# Írjon egy programot, ami kiszámolja egy adott hosszúságú matematikai inga periódusidejét
# A periódusidő számolására szolgáló formula a következő:  T =2 
# ahol : l az inga hossza és g a szabadesés gyorsulása a kísérlet helyén.


import math

l=float(input('Add meg az inga hosszát: '))
g=9.81
period=2*math.pi*math.sqrt(l/g)

print(period)
