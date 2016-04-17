#!/usr/bin/python2

import argparse
import time
from dotstar.dotstar import Adafruit_DotStar

parser = argparse.ArgumentParser()
parser.add_argument("led", help="index of led", type=int)
offGroup = parser.add_mutually_exclusive_group()
offGroup.add_argument("--off", help="turns off LED", action="store_true")
offGroup.add_argument("--alloff", help="turns off all LEDs", action="store_true")
parser.add_argument("-r", "--red", type=int, help="amount of red [0:255]")
parser.add_argument("-g", "--green", type=int, help="amount of green [0:255]")
parser.add_argument("-b", "--blue", type=int, help="amount of blue [0:255]")

args = parser.parse_args()

numpixels = 30
datapin   = 20
clockpin  = 21
strip     = Adafruit_DotStar(numpixels, datapin, clockpin)


strip.begin()
strip.setBrightness(64)

if args.alloff:
    for x in range(0, numpixels-1):
        strip.setPixelColor(x, 0)
    strip.show()
else:
    led = args.led
    color = 0x00
    if args.red:
        color = color | (args.red << 8)
    if args.green:
        color = color | (args.green << 16)
    if args.blue:
        color = color | args.blue

    if args.off:
        color = 0

    strip.setPixelColor(args.led, color)

    while True:
        strip.show()
        time.sleep(1.0/25)
