# This code scans any I2C devices connected to I2C0 & I2C1 at frequency 100kHz
# and print the address(es) on serial.
# ---
# Connection: I2C0, SCL0 = GP1, SDA0 = GP0
#             I2C1, SCL1 = GP3, SDA1 = GP2
# ---
# Hardware: Any RP2040 boards.
# ---
import machine

i2c0 = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0), freq=100000)
i2c1 = machine.I2C(1, scl=machine.Pin(3), sda=machine.Pin(2), freq=100000)

devices = i2c0.scan()
if devices:
    for d in devices:
        print("i2c0:")
        print(hex(d))
        
devices = i2c1.scan()
if devices:
    for d in devices:
        print("\ni2c1:")
        print(hex(d))