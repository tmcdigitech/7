import board, neopixel, time, digitalio


pixpin = board.GP28
numpix = 3
pixels = neopixel.NeoPixel(
    pixpin, numpix, brightness=1, auto_write=True, pixel_order=neopixel.GRBW
)

sensor_pin = board.GP18
# Enable internal pullup resistor on sensor pin
pin = digitalio.DigitalInOut(sensor_pin)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

RED = (200, 0, 0, 0)
GREEN = (0, 255, 0, 0)
BLUE = (0, 0, 200, 0)
WHITE = (0, 0, 0, 200)
OFF = (0, 0, 0, 0)

while True:
    print(
        pin.value,
    )
    if pin.value:
        pixels.fill(RED)
        time.sleep(2)
        pixels.fill(GREEN)
        time.sleep(2)
        pixels.fill(BLUE)
        time.sleep(2)
        pixels.fill(WHITE)
        time.sleep(2)

    else:
        pixels.fill(OFF)
