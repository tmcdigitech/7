---
title: Basic night light
weight: 10
---

Make a simple night-light using the built-in LED and a photocell on pin 18.

```python {linenos=table}
from digitalio import DigitalInOut, Direction
import board
import time

# Built in LED
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

sensor_pin = board.GP18
# Enable internal pullup resistor on sensor pin
pin = digitalio.DigitalInOut(sensor_pin)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP


while True:
    if pin.value:
        led.value = True
    else:
        led.value = False
    time.sleep(0.5)
```
