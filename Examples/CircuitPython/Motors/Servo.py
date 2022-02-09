import time
import board
import digitalio
import pwmio
from adafruit_motor import servo

# Initialize buttons as digital input.
button1 = digitalio.DigitalInOut(board.GP20)
button1.direction = digitalio.Direction.INPUT
button2 = digitalio.DigitalInOut(board.GP21)
button2.direction = digitalio.Direction.INPUT

# create a PWMOut object on the control pin.
pwm1 = pwmio.PWMOut(board.GP12, duty_cycle=0, frequency=50)
pwm2 = pwmio.PWMOut(board.GP13, duty_cycle=0, frequency=50)
pwm3 = pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=50)
pwm4 = pwmio.PWMOut(board.GP15, duty_cycle=0, frequency=50)

# You might need to calibrate the min_pulse (pulse at 0 degrees) and max_pulse (pulse at 180 degrees) to get accurate servo angle.
# The pulse range is 750 - 2250 by default (if not defined).

# You can also define the expected angle range:-
# servo = servo.Servo(board.D5, actuation_range=135)

# Initialize Servo objects.
servo1 = servo.Servo(pwm1, min_pulse=580, max_pulse=2700)
servo2 = servo.Servo(pwm2, min_pulse=580, max_pulse=2700)
servo3 = servo.Servo(pwm3, min_pulse=580, max_pulse=2700)
servo4 = servo.Servo(pwm4, min_pulse=580, max_pulse=2700)
angle = 0

while True:
    print (angle)
    # Read buttons' values.
    if not button1.value:
        angle += 5
    if not button2.value:
        angle -= 5

    # Limit the angle from 0 to 180 degrees.
    if angle > 180:
        angle = 180
    if angle < 0:
        angle = 0

    # Update servo angles.
    servo1.angle = servo2.angle = servo3.angle = servo4.angle = angle

    # Delay a bit to allow servo to move.
    time.sleep(0.01)

