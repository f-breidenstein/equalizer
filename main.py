#! /usr/bin/env python3
from lib import Equalizer

def main():
	eq = Equalizer.Equalizer(5,5)
	eq.clear()
	eq.set(0,1)
	eq.set(1,2)
	eq.set(2,3)
	eq.set(3,4)
	eq.set(4,5)


if __name__ == "__main__":
    main()
