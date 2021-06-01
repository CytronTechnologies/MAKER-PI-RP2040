# Setting Up MicroPython

### Why?
1. Update the MicroPython firmware on your Maker Pi RP2040 to the latest version.
2. Switch back to MicroPython after trying out CircuitPython, C/C++ and so on.

## Step 1
Connect Maker Pi RP2040 to your computer with a USB Micro B cable. Turn **ON** the power switch.

## Step 2
While holding down the **BOOT** button, press & release the reset **RST** button. You will see a new disk drive **RPI-RP2** appears on your computer. This means the board is now in bootloader mode. 
###### * You can also use any other methods to turn the board off and back on, while holding down the **BOOT** button to enter bootloader mode.

## Step 3
Download the latest [MicroPython firmware (UF2) for Raspberry Pi Pico](https://www.raspberrypi.org/documentation/rp2040/getting-started/#getting-started-with-micropython) to your computer. This file name should end with **.uf2** extension.

## Step 4
Copy the downloaded file onto the **RPI-RP2** drive. Once the firmware is uploaded completely, Maker Pi RP2040 will restart itself. You won't see a new disk drive appears on your computer, but with the right code editor and settings, you will be able to write your MicroPython code on Maker Pi RP2040 now! 

*to be continue...*

### Reference:
* https://www.tomshardware.com/how-to/raspberry-pi-pico-setup
