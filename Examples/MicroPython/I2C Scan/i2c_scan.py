# This code scans any I2C devices connected to I2C0 at frequency 100kHz
# and print the address(es) on serial.
# ---
# Connection: I2C0, SCL0 = GP1, SDA0 = GP0
# ---
# Hardware: Any RP2040 boards.
# ---
import machine

i2c0 = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0), freq=100000)

devices = i2c0.scan()
if devices:
    for d in devices:
        print("i2c0:")
        print(hex(d))