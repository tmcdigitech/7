import board, neopixel, time, digitalio

# Set up light strip
pixpin = board.GP28
numpix = 3
pixels = neopixel.NeoPixel(
    pixpin, numpix, brightness=0.3, auto_write=True, pixel_order=neopixel.GRB
)

# Set up light sensor pin
sensor_pin = board.GP16
pin = digitalio.DigitalInOut(sensor_pin)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

# Define our custom colours
# (r, g, b) with each value 0-255
# Google "color picker" for ideas!
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

while True:
    # Print a dot to check that it is going around the loop
    # Check this with the serial monitor if things aren't working
    print('.', end='')
    if pin.value:
        # It's dark
        pixels[0]= RED
        time.sleep(0.25)
        pixels[1] = GREEN
        time.sleep(0.25)
        pixels[2] = BLUE
        time.sleep(0.25)
        pixels.fill(WHITE)
        time.sleep(0.25)

    else:
        # It's light
        pixels.fill(OFF)
        pixels[0] = (10, 10, 10)
        time.sleep(0.1)
        pixels.fill(OFF)
        pixels[1] = (10, 10, 10)
        time.sleep(0.1)
        pixels.fill(OFF)
        pixels[2] = (10, 10, 10)
        time.sleep(0.1)
