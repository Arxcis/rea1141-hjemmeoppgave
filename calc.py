#!/usr/bin/python3
# -*- coding:utf-8 -*-

import math
MAX_KWH = 100
MILE_TO_KM = 0.6214; KM_TO_MILE = 1.609; 

def consumption_wh(kph):
	mph = kph / KM_TO_MILE
	return (0.0714*mph**2 - 3.523*mph + 239.203) * MILE_TO_KM

def total_consumption_kwh(kph, km):
	return consumption_wh(kph) * km / 10**3

def timesforbruk(kph, kilometer):
	return kilometer/kph

def soc(consumed, maxkwh):
	return (maxkwh-consumed) 

if __name__ == "__main__":
	print()

	for kph in range(40,101,5):
		print('{:2d}'.format(kph),"km/h\t", '{:8.2f}'.format(consumption_wh(kph)), "Wh/km")

	kilometer = 200
	print("Kjører "+str(kilometer)+"km i ulike hastigheter:")
	print("------------------------------------------------")
	print("  km/h    kWh       timer      SOC %")
	print("------------------------------------------------")

	for kph in range(40,101,5):
		print('   {:3d}'.format(kph),  
			  '\t  {:5.2f}'.format(total_consumption_kwh(kph, kilometer)), 
			  '\t{:5.2f}'.format(timesforbruk(kph,kilometer)),
			  '\t   {:5.2f}'.format(soc(total_consumption_kwh(kph, kilometer), MAX_KWH)))