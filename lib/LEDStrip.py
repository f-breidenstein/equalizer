import time
import math
import array
import fcntl

spidev = file("/dev/spidev0.0", "wb")
fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))

class LEDStrip:
    def __init__(self,size):
        this.size = size
        this.strip = []
        rgb = bytearray(3)
        for i in range(size):
            strip.append(rgb)


    def setColor(self,led,color):
        strip[pos] = color
        update()

    def clear(self):
        pass

    def update(self):
        for i in range(0, 25):
            spidev.write(strip[i])

        spidev.flush()
