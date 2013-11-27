# -*- coding: utf-8 -*-
# Gyakorlat 6.1.
# Írjon egy programot, ami m/sec és km/h ­ba számolja át a felhasználó által mérföld/h ­ban megadott 
# sebességet. .  ( 1 mérföld = 1609 méter)

mph=float(input('Adjon meg egy mph sebességet: '))
kmh=mph*1.609
mps=mph*0.44704
print(kmh,'Km/h')
print(mps,'Méter/s')
