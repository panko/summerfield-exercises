# -*- coding: utf-8 -*-
# Gyakorlat 5.10.
# Írjon egy kis programot, ami egy új t3 listát hoz létre. Ennek felváltva kell tartalmazni a két 
# lista   minden   elemét   úgy,   hogy   minden   hónap   nevét   követnie   kell   a   megfelelő   napok 
# számának : ['Január',31,'Február',28,'Március',31, stb...].

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
t3 = []
for i in range(len(t2)):
	t3.append(t2[i])
	t3.append(t1[i])

print(t3)
