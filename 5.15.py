# -*- coding: utf-8 -*-
# Gyakorlat 5.15.
# Írjon egy programot, ami egy szavakból álló lista elemeit egyenként megvizsgálja azért, 
# hogy két új listát hozzon létre. (például: ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean­Pierre', 
# 'Sandra'] Az egyikben 6 karakternél rövidebb szavakat legyenek, a másikban 6, vagy annál 
# több karaktert tartalmazzonó szavak legyenek.  

lista = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'JeanPierre', 'Sandra']
kisebbhatnal = []
nagyobbhatnal = []
for i in lista:
	if len(i) < 6:
		kisebbhatnal.append(i)
	else:
		nagyobbhatnal.append(i)

print(kisebbhatnal)
print(nagyobbhatnal)
