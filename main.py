#! /usr/bin/env python3
from lib import Equalizer
from random import randrange
from time import sleep

def main():
	eq = Equalizer.Equalizer(5,5)
	eq.clear()
	while (True):
		eq.clear()
		eq.set(0,randrange(6))
		eq.set(1,randrange(6))
		eq.set(2,randrange(6))
		eq.set(3,randrange(6))
		eq.set(4,randrange(6))
		eq.update()
		sleep(0.2)



if __name__ == "__main__":
    main()
