import machine
import utime

# Setup DC Motor pins
M1A = machine.PWM(machine.Pin(8))
M1B = machine.PWM(machine.Pin(9))
M2A = machine.PWM(machine.Pin(10))
M2B = machine.PWM(machine.Pin(11))
M1A.freq(50)
M1B.freq(50)
M2A.freq(50)
M2B.freq(50)

while True:
    print("Forward slow")
    M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
    M1B.duty_u16(30000)
    M2A.duty_u16(0)
    M2B.duty_u16(30000)
    utime.sleep(1)

    print("Stop")
    M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(0)
    utime.sleep(1)

    print("Forward")
    M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
    M1B.duty_u16(65535)
    M2A.duty_u16(0)
    M2B.duty_u16(65535)
    utime.sleep(1)

    print("Stop")
    M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(0)
    utime.sleep(1)

    print("Backward")
    M1A.duty_u16(65535)     # Duty Cycle must be between 0 until 65535
    M1B.duty_u16(0)
    M2A.duty_u16(65535)
    M2B.duty_u16(0)
    utime.sleep(1)

    print("Stop")
    M1A.duty_u16(0)     # Duty Cycle must be between 0 until 65535
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(0)
    utime.sleep(1)

    print("Backward slow")
    M1A.duty_u16(30000)     # Duty Cycle must be between 0 until 65535
    M1B.duty_u16(0)
    M2A.duty_u16(30000)
    M2B.duty_u16(0)
    utime.sleep(1)

    print("Brake")
    M1A.duty_u16(65535)     # Duty Cycle must be between 0 until 65535
    M1B.duty_u16(65535)
    M2A.duty_u16(65535)
    M2B.duty_u16(65535)
    utime.sleep(1)


