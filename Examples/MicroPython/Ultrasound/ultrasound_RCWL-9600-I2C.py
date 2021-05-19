# This code reads the distance using HC-SR04P (3-5V) ultrasonic sensor
# via I2C mode and print out the distance on serial. This ultrasound sensor
# uses RCWL-9600 IC and support default (trig-echo), I2C and UART modes.
# ---
# Modification: Solder a 10kOhm resistor across R4 pads at the bottom layer
#               of the sensor to enable I2C mode.
# ---
# Connection: I2C1, SCL1 = GP3, SDA1 = GP2
# ---
# Hardware:
# 1. Cytron Maker Pi RP2040 (www.cytron.io/p-MAKER-PI-RP2040)
#    - Any RP2040 boards should work too.
# 2. HC-SR04P (3-5V) ultrasonic (www.cytron.io/p-SN-HC-SR04P)
# ---
import machine
import utime


# init i2c1 at frequency 120kHz.
i2c = machine.I2C(1, scl=machine.Pin(3), sda=machine.Pin(2), freq=120000)
device_addr = 0x57

utime.sleep_ms(100)

while True:
    # write 0x01 to start ultrasound sensor
    i2c.writeto(device_addr, b'\x01')
    utime.sleep_ms(300)
    
    # read 3 bytes from ultrasound sensor
    data = bytearray(3)
    i2c.readfrom_into(device_addr, data)
    
    # convert to distance in cm
    distance = ((data[0]<<16)+(data[1]<<8)+data[2])/1000
    print(distance)
    utime.sleep_ms(200)