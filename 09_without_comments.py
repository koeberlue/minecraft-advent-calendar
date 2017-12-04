#!/usr/bin/python
import mcpi.minecraft
import mcpi.block
import RPi.GPIO
import time

minecraft = mcpi.minecraft.Minecraft.create()
blue = 18
button = 20

def ledOn(port):
  RPi.GPIO.output(port, True)

def ledOff(port):
  RPi.GPIO.output(port, False)

def changeBlocks(material):
  minecraft.setBlocks(-8, 4, 5, -7, 4, 4, material)

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(blue, RPi.GPIO.OUT, initial=False)
RPi.GPIO.setup(button, RPi.GPIO.IN)

try:
  while True:
    if RPi.GPIO.input(button) == False:
      ledOn(blue)
      changeBlocks(mcpi.block.DIAMOND_ORE)
    else:
      ledOff(blue)
      changeBlocks(mcpi.block.STONE)
    time.sleep(0.05)

except KeyboardInterrupt:
    RPi.GPIO.cleanup()
