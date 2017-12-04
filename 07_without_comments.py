#!/usr/bin/python
import mcpi.minecraft
import mcpi.block
import RPi.GPIO
import time

minecraft = mcpi.minecraft.Minecraft.create()
LED = 23

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(LED, RPi.GPIO.OUT, initial=False)

brightness = 0
lightControl = RPi.GPIO.PWM(LED, 50)
lightControl.start(brightness)

try:
  while True:
    hits = minecraft.events.pollBlockHits()
    for hit in hits:
      block = minecraft.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
      if block.id == mcpi.block.GOLD_ORE.id and brightness < 100:
        brightness += 10
      if block.id == mcpi.block.IRON_ORE.id and brightness > 0:
        brightness -= 10
      lightControl.ChangeDutyCycle(brightness)
      time.sleep(0.1)

except KeyboardInterrupt:
    lightControl.stop()
    RPi.GPIO.cleanup()
