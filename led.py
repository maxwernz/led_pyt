#!/usr/bin/python3

from PIL import ImageColor
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 168
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

def col_to_hex(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)


def hex_to_col(hex):
    return ImageColor.getrgb(hex)
    
if __name__=='__main__':
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    for i in range(LED_COUNT+1):
        strip.setPixelColorRGB(i, 255, 0, 0)