#!/usr/bin/python
import mcpi.minecraft
import mcpi.block
import RPi.GPIO
import time

minecraft = mcpi.minecraft.Minecraft.create()
red = 18
yellow = 23
green = 25
blue = 7
lights = [red, green, yellow, blue]

def ledOn(port):
    RPi.GPIO.output(port, True)

def ledOff(port):
    RPi.GPIO.output(port, False)


RPi.GPIO.setmode(RPi.GPIO.BCM)
for light in lights:
    RPi.GPIO.setup(light, RPi.GPIO.OUT, initial=False)

try:
    while True:
        hits = minecraft.events.pollBlockHits()
        for hit in hits:
            block = minecraft.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
            if block.id == mcpi.block.GOLD_ORE.id:
                for light in lights:
                    ledOn(light)
                    time.sleep(0.05)
                    ledOff(light)

except KeyboardInterrupt:
    RPi.GPIO.cleanup()
