# *************************************************
# Out-of-the-box Demo for Cytron Maker Pi RP2040
# 
# This demo code is written in CircuitPython and it serves
# as an easy quality check when you first receive the board.
#
# It plays a melody upon power up (slide power switch to ON)
# and shows running lights (blue LEDs) at the same time.
# Then the two RGB LEDs will animate the colors, while the 
# program checking push buttons' state, repeatedly.
# 
# Press GP20 button to play a short melody, lights up all 
# blue LEDs, move servo motors to 0 degree and run DC motors
# at 50% and -50% speeds.
# Press GP21 button to play another melody, turn off all blue 
# LEDs, move servo motors to 180 degree & brake DC motors.
# 
# Maker Pi RP2040 also has four DC motors quick test buttons 
# built-in. You may press the onboard M1A, M1B, M2A or M2B 
# push buttons to run your motors without writing any code.
#
# More info: 
# http://www.cytron.io/p-maker-pi-rp2040
# https://circuitpython.org/board/raspberry_pi_pico
#
# Email: support@cytron.io
# *************************************************
import board
import digitalio
import neopixel
import simpleio
import time
import pwmio
from adafruit_motor import servo, motor

# Initialize LEDs
# LEDs placement on Maker Pi RP2040
LED_PINS = [board.GP0, 
            board.GP1,
            board.GP2,
            board.GP3,
            board.GP4,
            board.GP5,
            board.GP6,
            board.GP7,
            board.GP16,
            board.GP17,
            board.GP26,
            board.GP27,
            board.GP28]

LEDS = []
for pin in LED_PINS:
    # Set pins as digital output
    digout = digitalio.DigitalInOut(pin)
    digout.direction = digitalio.Direction.OUTPUT
    LEDS.append(digout)

# Initialize Neopixel RGB LEDs
pixels = neopixel.NeoPixel(board.GP18, 2)
pixels.fill(0)

# Melody
MELODY_NOTE = [659, 659, 0, 659, 0, 523, 659, 0, 784]
MELODY_DURATION = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.2]

# Define pin connected to piezo buzzer
PIEZO_PIN = board.GP22

# Initialize buttons
btn1 = digitalio.DigitalInOut(board.GP20)
btn2 = digitalio.DigitalInOut(board.GP21)
btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP
btn2.pull = digitalio.Pull.UP

# Initialize servos
# 50% duty cycle: 2**15 = 32768 = 1/2 of 65536 (16-bit)
servo_motors = []  # create an array and add servo objects.
servo_motors.append(servo.Servo(pwmio.PWMOut(board.GP12, duty_cycle=2**15, frequency=50)))
servo_motors.append(servo.Servo(pwmio.PWMOut(board.GP13, duty_cycle=2**15, frequency=50)))
servo_motors.append(servo.Servo(pwmio.PWMOut(board.GP14, duty_cycle=2**15, frequency=50)))
servo_motors.append(servo.Servo(pwmio.PWMOut(board.GP15, duty_cycle=2**15, frequency=50)))

# Initialize DC motors
m1a = pwmio.PWMOut(board.GP8, frequency=10000)
m1b = pwmio.PWMOut(board.GP9, frequency=10000)
motor1 = motor.DCMotor(m1a, m1b)
m2a = pwmio.PWMOut(board.GP10, frequency=10000)
m2b = pwmio.PWMOut(board.GP11, frequency=10000)
motor2 = motor.DCMotor(m2a, m2b)

# -------------------------------------------------
# ON START: Show running light and play melody
# -------------------------------------------------
for i in range(len(LEDS)):
    LEDS[i].value = True
    
    if i < len(MELODY_NOTE):
        # Play melody tones
        simpleio.tone(PIEZO_PIN, MELODY_NOTE[i], duration=MELODY_DURATION[i])
    else:
        # Light up the remainding LEDs
        time.sleep(0.15)

# Turn off LEDs one-by-one very quickly
for i in range(len(LEDS)):
    LEDS[i].value = False
    time.sleep(0.02)


color = 0
state = 0

# -------------------------------------------------
# FOREVER LOOP: Check buttons & animate RGB LEDs
# -------------------------------------------------
while True:
    
    # Check button 1 (GP20)
    if not btn1.value:  # button 1 pressed
        # Light up all LEDs
        for i in range(len(LEDS)):
            LEDS[i].value = True
            
        # Move servos to 0 degree
        for i in range(len(servo_motors)):
            servo_motors[i].angle = 0
            
        # Move motors at 50% speed
        motor1.throttle = 0.5  # motor1.throttle = 1 or -1 for full speed
        motor2.throttle = -0.5
        
        # Play tones
        simpleio.tone(PIEZO_PIN, 262, duration=0.1)
        simpleio.tone(PIEZO_PIN, 659, duration=0.15)
        simpleio.tone(PIEZO_PIN, 784, duration=0.2)
        
    # Check button 2 (GP21)
    elif not btn2.value:  # button 2 pressed
        # Turn off all LEDs
        for i in range(len(LEDS)):
            LEDS[i].value = False
            
        # Move servos to 180 degree
        for i in range(len(servo_motors)):
            servo_motors[i].angle = 180
            
        # Brake motors
        motor1.throttle = 0  # motor1.throttle = None to spin freely
        motor2.throttle = 0
        
        # Play tones
        simpleio.tone(PIEZO_PIN, 784, duration=0.1)
        simpleio.tone(PIEZO_PIN, 659, duration=0.15)
        simpleio.tone(PIEZO_PIN, 262, duration=0.2)
        
        
    # Animate RGB LEDs
    if state == 0:
        if color < 0x101010:
            color += 0x010101   # increase rgb colors to 0x10 each
        else:
            state += 1
    elif state == 1:
        if (color & 0x00FF00) > 0:
            color -= 0x000100   # decrease green to zero
        else:
            state += 1
    elif state == 2:
        if (color & 0xFF0000) > 0:
            color -= 0x010000   # decrease red to zero
        else:
            state += 1
    elif state == 3:
        if (color & 0x00FF00) < 0x1000:
            color += 0x000100   # increase green to 0x10
        else:
            state += 1
    elif state == 4:
        if (color & 0x0000FF) > 0:
            color -= 1          # decrease blue to zero
        else:
            state += 1
    elif state == 5:
        if (color & 0xFF0000) < 0x100000:
            color += 0x010000   # increase red to 0x10
        else:
            state += 1
    elif state == 6:
        if (color & 0x00FF00) > 0:
            color -= 0x000100   # decrease green to zero
        else:
            state += 1
    elif state == 7:
        if (color & 0x00FFFF) < 0x001010:
            color += 0x000101   # increase gb to 0x10
        else:
            state = 1
    pixels.fill(color)  # fill the color on both RGB LEDs
    
    
    # Sleep to debounce buttons & change the speed of RGB color swipe
    time.sleep(0.05)
