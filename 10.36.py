# -*- coding: utf-8 -*-
# Gyakorlat 10.36

t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Január','Február','Március','Április','Május','Június',
 'Július','Augusztus','Szeptember','Október','November','December']
t3 = []
# t3.append(t1[0])
for i in range(12):
	t3.append(t2[i])
	t3.append(t1[i])
print(t3)
