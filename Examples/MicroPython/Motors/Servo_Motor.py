import machine
import utime

# Setup button pins
button1 = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Setup Servo Motor pins
pwm1 = machine.PWM(machine.Pin(12))
pwm2 = machine.PWM(machine.Pin(13))
pwm3 = machine.PWM(machine.Pin(14))
pwm4 = machine.PWM(machine.Pin(15))
pwm1.freq(50)
pwm2.freq(50)
pwm3.freq(50)
pwm4.freq(50)

angle = 0.0
min_dutycycle = 2200
max_dutycycle = 8300
dutycycle = 0

while True:
    print(angle)
    # Read buttons' values.
    if button1.value():
        angle += 5
    if button2.value():
        angle -= 5
    # Limit the angle from 0 to 180 degrees.
    if angle > 180:
        angle = 180.0
    if angle < 0:
        angle = 0.0

    dutycycle = int(((max_dutycycle - min_dutycycle) / 180) * angle) + min_dutycycle
    pwm1.duty_u16(dutycycle)
    pwm2.duty_u16(dutycycle)
    pwm3.duty_u16(dutycycle)
    pwm4.duty_u16(dutycycle)
    utime.sleep(0.01)
