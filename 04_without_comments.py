#!/usr/bin/python

import mcpi.minecraft
import mcpi.block
import RPi.GPIO
import time

blue = 18
minecraft = mcpi.minecraft.Minecraft.create()

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(blue, RPi.GPIO.OUT, initial=False)

def ledOn(port):
    RPi.GPIO.output(port, True)

def ledOff(port):
    RPi.GPIO.output(port, False)
    

try:
    while True:
        position = minecraft.player.getTilePos()
        material = minecraft.getBlock(position.x, position.y, position.z)
        if material != mcpi.block.SNOW.id:
            ledOn(blue)
            time.sleep(0.1)
            ledOff(blue)
            minecraft.setBlock(position.x, position.y, position.z, mcpi.block.SNOW)
        
except KeyboardInterrupt:
    RPi.GPIO.cleanup()
