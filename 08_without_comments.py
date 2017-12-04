#!/usr/bin/python
import mcpi.minecraft
import RPi.GPIO

mc = mcpi.minecraft.Minecraft.create()

red = 18
yellow = 23
green = 25
blue = 7
lights = [red, yellow, green, blue]

def ledOn(port):
    RPi.GPIO.output(port, True)

def ledOff(port):
    RPi.GPIO.output(port, False)


RPi.GPIO.setmode(RPi.GPIO.BCM)

for light in lights:
    RPi.GPIO.setup(light, RPi.GPIO.OUT, initial=False)

try:
    while True:
        position = mc.player.getTilePos()

        for light in lights:
            ledOff(light)
            
        if position.y <= 4:
            ledOn(blue)
        elif position.y <= 6:
            ledOn(green)
        elif position.y <= 8:
            ledOn(yellow)
        else:
            ledOn(red)

except KeyboardInterrupt:
    RPi.GPIO.cleanup()
