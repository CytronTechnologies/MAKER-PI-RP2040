# This code reads the analog value on GP26 and print out on serial.
# ---
# Connection: Analog In = GP26
# ---
# Hardware:
# 1. Cytron Maker Pi RP2040 (www.cytron.io/p-MAKER-PI-RP2040)
#    - Any RP2040 boards should work too.
# ---
import machine
import utime

analog = machine.ADC(26)

while True:
    print(analog.read_u16())
    utime.sleep(0.2)