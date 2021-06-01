# Setting Up CircuitPython

### Why?
1. Update the CircuitPython firmware on your Maker Pi RP2040 to the latest version.
2. Switch back to CircuitPython after trying out MicroPython, C/C++ and so on.

## Step 1
Connect Maker Pi RP2040 to your computer with a USB Micro B cable. Turn **ON** the power switch.

## Step 2
While holding down the **BOOT** button, press & release the reset **RST** button. You will see a new disk drive **RPI-RP2** appears on your computer. This means the board is now in bootloader mode. 
###### * You can also use any other methods to turn the board off and back on, while holding down the **BOOT** button to enter bootloader mode.

## Step 3
Download the latest [CircuitPython firmware for Raspberry Pi Pico](https://learn.adafruit.com/welcome-to-circuitpython) to your computer. This file name should end with **.uf2** extension.
###### * We're working on a custom CircuitPython firmware for Maker Pi RP2040 with the drivers needed to control the built-in features. Please stay tuned...

## Step 4
Copy the downloaded file onto the **RPI-RP2** drive. Once the firmware is uploaded completely, Maker Pi RP2040 will restart itself and a new **CIRCUITPY** drive appears on your computer. With that, you are ready to write your code on Maker Pi RP2040!

### Reference: 
* https://learn.adafruit.com/welcome-to-circuitpython/
