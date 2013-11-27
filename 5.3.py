# -*- coding: utf-8 -*-
# Gyakorlat 5.3.
# Írjon egy programot, ami Celsius fokokba számolja át a kiindulásul Fahrenheit fokokban 
# kifejezett hőmérsékletet és a fordított irányú átalakítást is elvégzi. .
# Az átalakítás képlete : T F =T C ×1,832 .

far=float(input('Add meg a hőmérsékletet farenheitben: '))

cel=(far-32)/1.8
print('{} C°'.format(round(cel, 2)))
