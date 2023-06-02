---
title: 7a Help getting started with project
---

## 1. Install firmware
1. Plug in your Pico.
2. If it appears as a USB drive called:
    - `RPI-RP2`, continue to step 3.
    - `CIRCUITPY`, skip to step 5.
3. Download the [CircuitPython firmware](https://downloads.circuitpython.org/bin/raspberry_pi_pico/en_US/adafruit-circuitpython-raspberry_pi_pico-en_US-8.0.5.uf2) and copy the file onto the `RPI-RP2` drive.
4. The Pico will automatically disconnect and reappear as a USB drive called CIRCUITPY.

## 2. Add library file
5. Download the [neopixel library](https://tmcdigitech.github.io/7/assessment/microcontrollers/7-project/neopixel.mpy) and copy it into the `lib` folder on the CIRCUITPY drive.

## 3. Open file and test code
6. Open Mu Editor.
7. Choose `Load`, and find the CIRCUITPY drive. Open the file called `code.py`. This is the program file the Pico is executing.
8. Find the [example programs](https://tmcdigitech.github.io/7/microcontrollers/02examples/) on the website.
9. Copy the code from the *Flash a light* example into the code.py file, replacing whatever is already there.
10. Save the file. The Pico will restart and run the new code automatically.
11. Check that the program is running correctly. In this case, the built-in green light next to the USB port should flash.
12. Change the sleep timings to adjust the flash pattern. Can you write your initials in [morse code](https://en.wikipedia.org/wiki/Morse_code)?

## 4. Solder components

9. Watch the [soldering tutorial](https://tmccatholiceduau-my.sharepoint.com/:v:/g/personal/aknight_tmc_catholic_edu_au/ESbtkG_fkwNArYszbg9YyEsBX8ulkV_4hPzuVSXzYMH4_w?e=ES3aD6).
10. Disconnect the USB cable from your Pico.
11. Solder the components onto your Pico, making absolutely sure that you follow the [wiring diagram](https://tmcdigitech.github.io/7/assessment/microcontrollers/7-project/picoLayout.png) and connect the correct pins to each other. Use the colour coding on the wires to check which pin on the strip is connected to which pin on the board.

## 5. Check your NeoPixel strip
12. Find the [Use NeoPixel strip](https://tmcdigitech.github.io/7/microcontrollers/02examples/neopixels/) example code on the website.
13. Copy the code from the example into the code.py file, replacing whatever is already there, and save it.
14. Check that the program is running correctly. In this case, the NeoPixels should light up variously in red, green, blue and white.
15. If this doesn't happen check that:
    - you have wired the strip correctly
    - you have added the neopixel library to the lib folder
    - the library file is called `neopixel.mpy` and not, for example `neopixel (1).mpy`.
