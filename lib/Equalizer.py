#! /usr/bin/env python3
from lib import LEDStrip
from colorsys import hsv_to_rgb

class Equalizer():

	def __init__(self,rowCount,colCount):
		self.rowCount = rowCount
		self.colCount = colCount
		self.columnColor = []
		self.calcColor()
		self.strip = LEDStrip.LEDStrip(25)
		self.columnNumbers = [[0,9,10,19,20],
							[1,8,11,18,21],
							[2,7,12,17,22],
							[3,6,13,16,23],
							[4,5,14,15,24]]

	def calcColor(self):
		block = float(300) / self.colCount
		for i in range(self.colCount):
			hue = i * block 
			hue = hue / 300
			r,g,b = hsv_to_rgb(hue,1,1)
			color = bytearray(3)
			color[0] = int(r)
			color[1] = int(g)
			color[2] = int(b)
			self.columnColor.append(color)

	def set(self,col,value):
		for idx,led in enumerate(self.columnNumbers[col]):

			if (idx <= value-1):
				color = self.columnColor[col]
				self.strip.setColor(led,color)
			else:
				break

	def clear(self):
		self.strip.clear()

	def update(self):
		self.strip.update() 
