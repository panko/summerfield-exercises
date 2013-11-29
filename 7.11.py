#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# kiíratom az n-edik hónap nevét.


def honapNeve(n):
	honapok=[None, "Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December"]
	return honapok[n]

print(honapNeve(9))
