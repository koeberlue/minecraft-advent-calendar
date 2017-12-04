#!/usr/bin/python
import mcpi.minecraft
import mcpi.block
import RPi.GPIO
import time

minecraft = mcpi.minecraft.Minecraft.create()
button = 8

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(button, RPi.GPIO.IN, RPi.GPIO.PUD_DOWN)

try:
    while True:
        if RPi.GPIO.input(button) == True:
            position = minecraft.player.getTilePos()
            minecraft.setBlocks(position.x-1, position.y, position.z-1, position.x+1, position.y, position.z+1, mcpi.block.SAND)
            minecraft.player.setPos(position.x, position.y+1, position.z)
            time.sleep(0.2)

except KeyboardInterrupt:
    RPi.GPIO.cleanup()
