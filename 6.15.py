# -*- coding: utf-8 -*-
# Gyakorlat 6.15.
# Írjon egy programhurkot, ami a felhasználótól kéri a tanulók érdemjegyeit. A hurok csak 
# akkor  fejeződjön be, ha a felhasználó  egy negatív  értéket ír be. Az így beírt jegyekkel 
# hozzon létre egy listát. Minden új jegy beírása után (tehát minden iterrációnál) írassa ki a 
# beírt jegyek számát, a legnagyobb és a legkisebb jegyet és a jegyek átlagát.
jegy=[]
ll=0
while 1==1:
	a=int(input('Adja meg a tanulók érdemjegyeit egyessével: '))
	if a <= 0:
		break
	ll+=a
	jegy.append(a)
	print('Eddig beírt jegyek száma:',len(jegy))
	print('Legnagyobb jegy:',max(jegy))
	print('Legkisebb jegy:',min(jegy))
	print('Jegyek átlaga:',ll/len(jegy))
	

