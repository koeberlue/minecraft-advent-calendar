#!/usr/bin/python

import mcpi.minecraft
import RPi.GPIO
import time

red = 18
yellow = 23
green = 25

minecraft = mcpi.minecraft.Minecraft.create()

def ledOn(port):
    RPi.GPIO.output(port, True)

def ledOff(port):
    RPi.GPIO.output(port, False)
    

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(red, RPi.GPIO.OUT, initial=True)
RPi.GPIO.setup(yellow, RPi.GPIO.OUT, initial=False)
RPi.GPIO.setup(green, RPi.GPIO.OUT, initial=False)

try:
    while True:
        position = minecraft.player.getTilePos()
        material = minecraft.getBlock(position.x, position.y-1, position.z)
        if material == 42:        
            ledOn(yellow)
            time.sleep(0.6)
            ledOff(red)
            ledOff(yellow)
            ledOn(green)
            time.sleep(2)
            ledOff(green)
            ledOn(yellow)
            time.sleep(0.6)
            ledOff(yellow)
            ledOn(red)
            time.sleep(2)

except KeyboardInterrupt:
    RPi.GPIO.cleanup()
        
    

        
