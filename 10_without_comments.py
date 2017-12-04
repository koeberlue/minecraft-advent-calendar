#!/usr/bin/python
import mcpi.minecraft
import mcpi.block
import RPi.GPIO

minecraft = mcpi.minecraft.Minecraft.create()

ledRed = 25
ledGreen = 24
ledBlue = 23

blockRedOff = 14
blockGreenOff = 13
blockBlueOff = 11

blockRedOn = 1
blockGreenOn = 5
blockBlueOn = 3

def ledOn(port):
  RPi.GPIO.output(port, True)

def ledOff(port):
  RPi.GPIO.output(port, False)

def setBlockColor(position, color):
  minecraft.setBlock(position.x, position.y, position.z, mcpi.block.WOOL.id, color)

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(ledRed, RPi.GPIO.OUT, initial=False)
RPi.GPIO.setup(ledGreen, RPi.GPIO.OUT, initial=False)
RPi.GPIO.setup(ledBlue, RPi.GPIO.OUT, initial=False)

try:
  while True:
    hits = minecraft.events.pollBlockHits()
    for hit in hits:
      block = minecraft.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
      if block.id == mcpi.block.WOOL.id:
        if block.data == blockRedOff:
          setBlockColor(hit.pos, blockRedOn)
          ledOn(ledRed)
        if block.data == blockRedOn:
          setBlockColor(hit.pos, blockRedOff)
          ledOff(ledRed)
        if block.data == blockGreenOff:
          setBlockColor(hit.pos, blockGreenOn)
          ledOn(ledGreen)
        if block.data == blockGreenOn:
          setBlockColor(hit.pos, blockGreenOff)
          ledOff(ledGreen)
        if block.data == blockBlueOff:
          setBlockColor(hit.pos, blockBlueOn)
          ledOn(ledBlue)
        if block.data == blockBlueOn:
          setBlockColor(hit.pos, blockBlueOff)
          ledOff(ledBlue)

except KeyboardInterrupt:
    RPi.GPIO.cleanup()
