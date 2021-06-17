# CYTRON MAKER PI RP2040
[Cytron Maker Pi RP2040](https://www.cytron.io/p-maker-pi-rp2040) features the first microcontroller designed by Raspberry Pi - [RP2040](https://www.raspberrypi.org/documentation/rp2040/getting-started/), embedded on a robot controller board. The board comes with dual channel DC motor driver, 4 servo motor ports and 7 Grove I/O connectors, ready for your next DIY robot / motion control project. Now you can build robot, while trying out the new RP2040 chip.

![Maker Pi RP2040](/maker-pi-rp2040-tagline.png)

## Out-of-the-box Experience
CircuitPython firmware and a [demo program](/Examples/CircuitPython/Out-of-the-box%20Demo%20Code/code.py) are preloaded on the Maker Pi RP2040 by default. Power up your board with a USB Micro B cable (or via LIPO / VIN) to try out.
- **On startup**:
   - play a melody tune
   - perform a sequential LED lighting (blue LEDs)
- **Forever loop**: 
   - RGB (Neopixel) LEDs perform color fading
- **Press GP20 push button**:
   - light up all blue LEDs
   - run DC Motor 1 forward and DC Motor 2 backward, both at 50% speed
   - move all Servo motors to 0 degree
- **Press GP21 push button**: 
   - turn off all blue LEDs
   - stop both DC Motor 1 & 2
   - move all Servo motors to 180 degree

This is very useful for checking the basic functionalities of the board for the first time.

## Getting Started & Examples
We provide some [example code](/Examples) in CircuitPython and MicroPython for your reference. Make sure the correct firmware is loaded on your Maker Pi RP2040 before you start coding with either languages.

### CircuitPython
We've created the [CircuitPython .UF2 firmware for Maker Pi RP2040](https://circuitpython.org/board/cytron_maker_pi_rp2040/) with helps from the awesome folks at CircuitPython and Adafruit. It includes the libraries to work with Maker Pi RP2040's built-in features, eg. DC & servo motors control and Neopixel LEDs. The [adafruit_motor](https://github.com/adafruit/Adafruit_CircuitPython_Motor), [neopixel](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel) and [simpleio](https://github.com/adafruit/Adafruit_CircuitPython_SimpleIO) libraries are embedded by default, so there's no need to add them to the _lib_ folder of the _CIRCUITPY_ drive manually.

Follow [this guide](/setup-circuitpython.md) to load the CircuitPython firmware on your Maker Pi RP2040.
If you see _CIRCUITPY_ drive appears on your computer, it means CircuitPython firmware is already loaded on board and you are good to go! 

The _code.py_ file on the _CIRCUITPY_ drive (of any new Maker Pi RP2040) is the demo program which comes with the board. You can open this file with any code editor to view or modify it. [Mu Editor](https://codewith.mu/) is highly recommended for coding the CircuitPython. Follow [Adafruit's guide](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor) to install the software.

Besides modifying the demo program, you can also open one of the [CircuitPython examples here](/Examples/CircuitPython). You can copy the code and paste it in the _code.py_ file on your _CIRCUITPY_ drive. Save the file after making desired changes and the code will run as soon as the file is done saving.
> Please wait until the file is successfully saved before resetting or unplugging your board!



### MicroPython

Follow [this guide](https://www.raspberrypi.org/documentation/rp2040/getting-started/#getting-started-with-micropython) to load the MicroPython firmware on your Maker Pi RP2040.



## Reference:

- [Maker Pi RP2040 Product Page](https://www.cytron.io/p-maker-pi-rp2040)
- [Maker Pi RP2040 Datasheet](https://docs.google.com/document/d/1DJASwxgbattM37V4AIlJVR4pxukq0up25LppA8-z_AY/edit?usp=sharing)
- [RP2040 Datasheet](https://datasheets.raspberrypi.org/rp2040/rp2040-datasheet.pdf)
- [Download CircuitPython for Maker Pi RP2040](https://circuitpython.org/board/cytron_maker_pi_rp2040/)
