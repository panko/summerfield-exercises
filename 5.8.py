# -*- coding: utf-8 -*-
# Gyakorlat 5.8.
# Írjon egy programot, ami egy új változóba másol át egy karakterláncot úgy, hogy csillagot 
# szúr be a karakterek közé.
# Így például, « gaston »­ból « g*a*s*t*o*n » lesz.

text=input('Irjon be egy szöveget: ')
result=text[0]
a=1
for i in range(len(text)-1):
	result+='*'
	result+=text[a]
	a+=1
	
print(result)
