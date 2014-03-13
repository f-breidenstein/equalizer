#! /usr/bin/env python
from LEDStrip import *
from colorsys import hsv_to_rgb

class Equalizer():

    def __init__(self,rowCount,colCount):
        this.rowCount = rowCount
        this.colCount = colCount
        this.columnColor = calcColor(colCount)
        this.strip = Strip(25)
        this.columNumbers = [[0,9,10,19,20],
                            [1,8,11,18,21],
                            [2,7,12,17,22],
                            [3,6,13,16,23],
                            [4,5,14,15,24]]


    def calcColor(self):
        b = float(240) / this.colCount
        for i in range(this.colCount):
            hue = i * b + int(float(b)/2)
            hue = hue / 240
            r,g,b = hsv_to_rgb(hue,1,1)
            color = bytearray(3)
            color[0] = r
            color[1] = g
            color[2] = b
            this.columnColor[i] = color

    def set(self,col,value):
        for idx,led in enumerate(this.columnNumbers[col]):
            if (idx <= value):
                this.strip.setLed(led,this.columnColor[col])
            else:
                break
        this.stip.update() 

    def clear(self):
        this.strip.clear()

