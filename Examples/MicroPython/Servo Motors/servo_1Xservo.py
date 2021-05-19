# This code controls one servos to move from 0 degree to 180 degree,
# then back to 0 degree, and repeats forever.
# ---
# Connection: 1x Servo ports at GP12. Take note on the polarity.
# ---
# Hardware:
# 1. Cytron Maker Pi RP2040 (www.cytron.io/p-MAKER-PI-RP2040)
#    - Any RP2040 boards should work too.
# 2. TS90A Micro Servo 3-6V (www.cytron.io/p-analog-micro-servo-9g-3v-6v)
#    - Any servo motors within the rated voltage of 3.6-6V. 
# ---
from machine import Pin, PWM
import time

# fine tune the duty cycle values to suit your servo motor
MIN_DUTY = 1600
MAX_DUTY = 8400

pwm = PWM(Pin(12))
pwm.freq(50)

while True:
    pwm.duty_u16(MIN_DUTY)
    time.sleep_ms(1000)
    pwm.duty_u16(MAX_DUTY)
    time.sleep_ms(1000)