#!/usr/bin/python3

from rpi_ws281x import PixelStrip, Color
import sys

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
    return (int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:], 16))


if __name__=='__main__':
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    args = sys.argv[1:]

    if args == []:
        color = "#ff2200"
    else:
        color = hex_to_col("#" + args[0])
    for i in range(LED_COUNT+1):
        strip.setPixelColorRGB(i, *color)
        strip.show()