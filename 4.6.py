# -*- coding: utf-8 -*-
# 4.6
# Írjon egy programot, ami átszámolja a kiindulásként megadott egészszámú másodpercet 
# évekké, hónapokká, napokká, percekké és másodpercekké.
# (Használja a modulo operátort : % ).

intsecond=int(input('Egésszámú másodperc: '))


# egy napi másodpercek
ns=3600*24
# egy évi másodpercek
ys=ns*365
# honapra eső másodpercek 
ms=ns*30
# evek
ysf=intsecond//ys	#adatok alapjan evek szama
maradek_y=intsecond%ys
# honap
msf=maradek_y//ms
maradek_m=maradek_y%ms

# napok
dsf=maradek_m//ns
maradek_d=maradek_m%ns

# ora
hsf=maradek_d//3600
maradek_h=maradek_d%3600

#perc
misf=maradek_h//60
maradek_mi=maradek_h%60


print('Evek szama: {}'.format(ysf))
print('Honapok szama: {}'.format(msf))
print('Napok szama: {}'.format(dsf))
print('Orak szama: {}'.format(hsf))
print('Percek szama: {}'.format(misf))
print('Masodpercek szama: {}'.format(maradek_mi))
