---
title: Use NeoPixel strip
weight: 20
---

```python
import board
import neopixel
import time
import digitalio

pixpin = board.GP28
numpix = 3
pixels = neopixel.NeoPixel(
    pixpin, numpix, brightness=1, auto_write=True, pixel_order=neopixel.GRBW
)

RED = (255, 0, 0, 0)
GREEN = (0, 255, 0, 0)
BLUE = (0, 0, 255, 0)
WHITE = (0, 0, 0, 200)
OFF = (0, 0, 0, 0)

while True:
    pixels[0] = RED
    time.sleep(0.5)
    pixels[1] = GREEN
    time.sleep(0.5)
    pixels[2] = BLUE
    time.sleep(1.5)
    pixels.fill(WHITE)
    time.sleep(0.5)
