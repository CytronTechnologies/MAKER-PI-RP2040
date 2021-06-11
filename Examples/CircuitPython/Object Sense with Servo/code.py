# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Tested with CircuitPython 6.3.0

Hardware:
- Maker Pi RP2040 https://my.cytron.io/p-maker-pi-pico
- M5Stack ToF VL53L0X Sensor Unit https://my.cytron.io/p-m5stack-tof-vl53l0x-sensor-unit
- RC Servo Motor (Metal Gear) https://my.cytron.io/p-rc-servo-motor-metal-gear
- USB Micro B Cable https://my.cytron.io/p-usb-micro-b-cable
- (Optional) LiPo Rechargeable Battery 3.7V 1300mAH https://my.cytron.io/p-lipo-rechargeable-battery-3.7v-1300mah

Additional libraries:
https://circuitpython.org/libraries
- adafruit_bus_device
- adafruit_motor
- adafruit_vl53l0x.mpy
- simpleio.mpy

Video:
https://youtu.be/-Os6Pl4O9NM

Last updated: 11 June 2021
"""

import time
import board
import digitalio
import simpleio
import busio
import pwmio
from adafruit_motor import servo
import adafruit_vl53l0x

button1 = digitalio.DigitalInOut(board.GP20)
button1.direction = digitalio.Direction.INPUT

piezo = board.GP22

# create a PWMOut object on Pin GP15.
pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.GP5, board.GP4)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Optionally adjust the measurement timing budget to change speed and accuracy.
# See the example here for more details:
#   https://github.com/pololu/vl53l0x-arduino/blob/master/examples/Single/Single.ino
# For example a higher speed but less accurate timing budget of 20ms:
# vl53.measurement_timing_budget = 20000
# Or a slower but more accurate timing budget of 200ms:
# vl53.measurement_timing_budget = 200000
# The default timing budget is 33ms, a good compromise of speed and accuracy.

INCREMENT = 2
DECREMENT = -2

servo_dir = INCREMENT
servo_pos = 90
prev_time = 0

simpleio.tone(piezo, 523, 0.1)

my_servo.angle = servo_pos

while button1.value:
    pass

# Main loop will read the range and print it every second.
while True:
    servo_pos = servo_pos + servo_dir
    if servo_pos == 0:
        servo_dir = INCREMENT
    elif servo_pos == 180:
        servo_dir = DECREMENT
    my_servo.angle = servo_pos

    distance = vl53.range
    print("Range: {0}mm".format(distance))

    if distance < 200:
        simpleio.tone(piezo, 600-distance, 0.05)

