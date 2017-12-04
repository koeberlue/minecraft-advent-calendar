#!/usr/bin/python

import mcpi.minecraft
import RPi.GPIO

red = 18
green = 23

minecraft = mcpi.minecraft.Minecraft.create()


RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(red, RPi.GPIO.OUT)
RPi.GPIO.setup(green, RPi.GPIO.OUT)

def ledOn(port):
    RPi.GPIO.output(port, True)

def ledOff(port):
    RPi.GPIO.output(port, False)

try:
    while True:
        position = minecraft.player.getTilePos()
        if (position.x<=18 and position.x>=16 and position.z<=8 and position.z >=6):
            ledOn(green)
            ledOff(red)
        else:
            ledOn(red)
            ledOff(green)
except KeyboardInterrupt:
    Rpi.GPIO.cleanup()
            
