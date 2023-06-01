---
title: Flash a light
weight: 10
---

The first project you do with any new piece of hardware: flash a light.

```python {linenos=table}
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.2)
    led.value = False
    time.sleep(0.8)
```
