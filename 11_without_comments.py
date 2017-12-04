#!/usr/bin/python
import mcpi.minecraft
import mcpi.block
import RPi.GPIO

minecraft = mcpi.minecraft.Minecraft.create()

red = 0
green = 1
blue = 2

lights = [25, 24, 23]

blockColorOff = [14, 13, 11]
blockColorOn = [1, 5, 3]

x = 0
y = 1
z = 2
positionRed = [-8, 3, 21]
positionGreen = [-9, 3, 21]
positionBlue = [-10, 3, 21]
positions = [positionRed, positionGreen, positionBlue]

RPi.GPIO.setmode(RPi.GPIO.BCM)
for light in lights:
  RPi.GPIO.setup(light, RPi.GPIO.OUT, initial = False)

lightControlRed = RPi.GPIO.PWM(lights[red], 50);
lightControlGreen = RPi.GPIO.PWM(lights[green], 50);
lightControlBlue = RPi.GPIO.PWM(lights[blue], 50);
lightControls = [lightControlRed, lightControlGreen, lightControlBlue]

for lightControl in lightControls:
  lightControl.start(0)

def setBlockColor(position, color):
  for counter in range(position.z - positions[color][z]):
    minecraft.setBlock(positions[color][x], positions[color][y], positions[color][z] + counter, mcpi.block.WOOL.id, blockColorOn[color])
  for counter in range(10 - position.z + positions[color][z]):
    minecraft.setBlock(positions[color][x], positions[color][y], position.z + counter, mcpi.block.WOOL.id, blockColorOff[color])

def setLedBrightness(brightness, color):
  lightControls[color].ChangeDutyCycle(brightness * 10)

try:
  while True:
    hits = minecraft.events.pollBlockHits()
    for hit in hits:
      block = minecraft.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
      if block.id == mcpi.block.WOOL.id:
        if hit.pos.x == positions[red][x]:
          setBlockColor(hit.pos, red)
          setLedBrightness(hit.pos.z - positions[red][z], red)
        if hit.pos.x == positions[green][x]:
          setBlockColor(hit.pos, green)
          setLedBrightness(hit.pos.z - positions[green][z], green)
        if hit.pos.x == positions[blue][x]:
          setBlockColor(hit.pos, blue)
          setLedBrightness(hit.pos.z - positions[blue][z], blue)

except KeyboardInterrupt:
    GPIO.cleanup()
