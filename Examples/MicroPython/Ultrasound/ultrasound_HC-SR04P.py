# This code reads the distance using HC-SR04P (3-5V) ultrasonic sensor
# via default (trig-echo) mode and print out on serial.
# ---
# Connection: TRIG = GP3, ECHO = GP2
# ---
# Hardware:
# 1. Cytron Maker Pi RP2040 (www.cytron.io/p-MAKER-PI-RP2040)
#    - Any RP2040 boards should work too.
# 2. HC-SR04P (3-5V) ultrasonic (www.cytron.io/p-SN-HC-SR04P)
# ---
from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

distance = 0
def ultrasound():
    global distance
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2

while True:
    ultrasound()
    print("Distance = ", distance, "cm")
    utime.sleep(0.5)