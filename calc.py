#!/usr/bin/python3
# -*- coding:utf-8 -*-

import math

mileTokm = 0.6214
KILOMETER_PER_MILE = 1.609


def consumption_mile(speed):
	return (0.0714*speed**2 - 3.523*speed + 239.203)

def consumption_km(speed):
	return consumption_mile(speed) * mileTokm / 10**3

def total_consumption(speed, kilometer):
	return (0.0714*speed**2 - 3.523*speed + 239.203) * kilometer * mileTokm / 10**3


if __name__ == "__main__":
	print()

	for speed in range(5,71,5):
		print('{:2d}'.format(speed),"km/h\t", '{:8.2f}'.format(consumption_km(speed)), "kWh/km")

	print("Forskjellige hastigheter kjører i 200km:")
	for speed in range(5,71,5):
		print(' {:2d}'.format(speed),"km/h\t",  '{:5.2f}'.format(total_consumption(speed, 200)), "kWh")