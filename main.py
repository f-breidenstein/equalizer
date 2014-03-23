#! /usr/bin/env python3
from lib import Equalizer
from random import randrange
from time import sleep

def main():
	eq = Equalizer.Equalizer(5,5)
	eq.clear()
	values = [0,0,0,0,0]
	while (True):
		eq.clear()
		for i in range(5):
			if randrange(2) == 0 and values[i] < 5: # +1
				values[i] = values[i] + 1
			elif values[i] > 0: # -1
				values[i] = values[i] - 1
			eq.set(i,values[i])

		eq.update()
		sleep(0.15)



if __name__ == "__main__":
    main()
