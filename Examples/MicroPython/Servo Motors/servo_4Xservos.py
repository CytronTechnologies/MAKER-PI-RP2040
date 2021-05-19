# This code controls all 4 servos to move from 0 degree to 180 degree,
# then back to 0 degree, and repeats forever.
# ---
# Connection: 4x Servo ports - from GP12 to GP15
# ---
# Hardware:
# 1. Cytron Maker Pi RP2040 (www.cytron.io/p-MAKER-PI-RP2040)
#    - Any RP2040 boards should work too.
# 2. TS90A Micro Servo 3-6V (www.cytron.io/p-analog-micro-servo-9g-3v-6v)
#    - Any servo motors within the rated voltage of 3.6-6V. 
# ---
from machine import Pin, PWM
import time

# fine tune the duty cycle values to suit your servo motors
MIN_DUTY = 1600
MAX_DUTY = 8400

servo1 = PWM(Pin(12))
servo1.freq(50)
servo2 = PWM(Pin(13))
servo2.freq(50)
servo3 = PWM(Pin(14))
servo3.freq(50)
servo4 = PWM(Pin(15))
servo4.freq(50)

while True:
    servo1.duty_u16(MIN_DUTY)
    servo2.duty_u16(MIN_DUTY)
    servo3.duty_u16(MIN_DUTY)
    servo4.duty_u16(MIN_DUTY)
    time.sleep_ms(1000)
    servo1.duty_u16(MAX_DUTY)
    servo2.duty_u16(MAX_DUTY)
    servo3.duty_u16(MAX_DUTY)
    servo4.duty_u16(MAX_DUTY)
    time.sleep_ms(1000)