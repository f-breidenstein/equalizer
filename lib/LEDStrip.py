#! /usr/bin/env python3
import time
import math
import array
import fcntl

spidev = open("/dev/spidev0.0", "wb")
fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))

class LEDStrip:
	def __init__(self,size):
		self.size = size
		self.strip = []
		rgb = bytearray(3)
		for i in range(size):
			self.strip.append(rgb)


	def setColor(self,led,color):
		self.strip[led] = color

	def clear(self):
		for i in range(self.size):
			self.strip[i][0] = 0
			self.strip[i][1] = 0
			self.strip[i][2] = 0
		self.update()

	def update(self):
		for i in range(self.size):
			spidev.write(self.strip[i])

		spidev.flush()
