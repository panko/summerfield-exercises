# -*- coding: utf-8 -*-
# Gyakorlat 5.14.
# Írjon   egy   programot,   ami   megvizsgálja   egy   számlista   minden   elemét   (például   az   előző 
# példa listáját) azért, hogy két új listát hozzon létre. Az egyik csak az eredeti lista páros 
# számait tartalmazza, a másik a páratlanokat. Például, ha a kiindulási lista az előző gyakorlat 
# listája, akkor a programnak egy  páros listát  kell létrehoznia, ami a  [32, 12, 8, 2]  ­t 
# tartalmazza és egy páratlan listát ami [5, 3, 75, 15] ­t tartalmazza. Trükk : Gondoljon 
# az előzőekben említett modulo (%) operátor használatára !

lista = [32, 5, 12, 8, 3, 75, 2, 15]
paros = []
paratlan = []
for i in range(len(lista)):
	if lista[i]%2 == 0:
		paros.append(lista[i])
	else:
		paratlan.append(lista[i])
print('A paros szamok: {}'.format(paros))
print('A paratlan szamok: {}'.format(paratlan))
