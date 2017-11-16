#!/usr/bin/python3
# -*- coding:utf-8 -*-

import math
MILE_TO_KM = 0.6214; KM_TO_MILE = 1.609; 

def consumption_kwh(kph):
	mph = kph / KM_TO_MILE
	# Coeffisients
	A = 0.0714
	B = 3.523
	C = 239.203
	# Function
	return (A*mph**2 - B*mph + C) * MILE_TO_KM / 10**3

def consumption_kwh_integrated(kph, km):
	return consumption_kwh(kph) * km

def travel_time(kph, kilometer):
	return kilometer/kph

def percent_to_kwh(maxkwh):
	return 100 / maxkwh

def SOC(maxkwh, consumedkwh):
	return (maxkwh-consumedkwh) / percent_to_kwh(maxkwh)

def charge_time_from_zero(soc):
	# Coeffisients
	A = 0.00289
	B = 0.4034
	C = 2.197
	# Function
	return  A*soc**2 + B*soc + C 

def charge_time(soc_end, soc_begin):
	return charge_time_from_zero(soc_end) - charge_time_from_zero(soc_begin)



if __name__ == "__main__":

	START_KWH = 100
	KILOMETER = 200

	print("Kjører "+str(KILOMETER)+"km i ulike hastigheter:")
	print("---------------------------------------------------------------------------------------")
	print("    km/h   kwh/km     kWh   Kjøretid[min]   SOC start    Lade 90%[min]    Total tid    ")
	print("---------------------------------------------------------------------------------------")

	for kph in range(40,181,10):

		_consumption_kwh 			= consumption_kwh(kph)
		_consumption_kwh_integrated = consumption_kwh_integrated(kph, KILOMETER)
		_travel_time 				= travel_time(kph,KILOMETER)*60
		_SOC_charge_begin 			= SOC(START_KWH, _consumption_kwh_integrated)
		_charge_time 				= charge_time(100, _SOC_charge_begin)
		_total_time 				= _travel_time + _charge_time

		print('\t{:3d}'.format(kph),
			  '\t{:4.3f}'.format(_consumption_kwh),
			  '\t{:6.2f}'.format(_consumption_kwh_integrated), 
			  '\t{:7d}'.format(round(_travel_time)),
			  '\t{:10.2f}'.format(_SOC_charge_begin),
			  '\t{:9d}'.format(round(_charge_time)),
			  '\t{:15d}'.format(round(_total_time)))
