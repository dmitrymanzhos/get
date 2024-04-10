import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

gp.setup(dac, gp.OUT, initial=gp.HIGH)
gp.setup(troyka, gp.OUT, initial=gp.HIGH)
gp.setup(comp, gp.IN)

def int_to_bin(a):
    return [int(i) for i in bin(a)[2:].rjust(8, '0')]

def adc():
    for i in range(0, 256):
        gp.output(dac, int_to_bin(i))
        if gp.input(comp) == 1:
            print(i)
            return i
    return 0


try:
    while True:
        v = adc()
        gp.output(dac, int_to_bin(v))
        print(f"{v}, {(3.3/256)*v} V")
     



finally:
    gp.output(dac, 0)
    gp.cleanup()