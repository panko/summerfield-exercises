# -*- coding: utf-8 -*-
# Gyakorlat 6.11.
# Kérjük   meg  a   felhasználót,   hogy   írjon   be   három   hosszúságadatot:   a,   b,   c   ­t.   Ennek   a   három 
# hosszúságnak   a   segítségével   határozza   meg,   hogy   lehet­e   egy   háromszöget   szerkeszteni.    Majd 
# határozza   meg,   hogy   ez   a  háromszög:   derékszögű,   egyenlőszárú,   egyenlőoldalú   vagy   általános 
# háromszög. Figyelem : egy derékszögű háromszög lehet egyenlőszárú.

a=int(input('Adja meg a háromszög a oldalát: '))
b=int(input('Adja meg a háromszög b oldalát: '))
c=int(input('Adja meg a háromszög c oldalát: '))

if a+b>c and a+c>b and b+c>a:
	print('Ez egy háromszög.')
else:
	print('Ez nem háromszög.')
if a==b or b==c or a==c:
	print('Ez egy egyenlőszárú háromszög.')
if a==b and b==c:
	print('Ez egy egyenlőoldalú háromszög.')
if (a**2+b**2==c**2) or (a**2+c**2==b**2) or (b**2+c**2==a**2):
	print('Ez egy derékszögú háromszög.')
if a!=c and b!=a and c!=b:
	print('ez egy általános háromszög')
