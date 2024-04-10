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
    al = [0 for i in range(8)]
    for i in range(8):
        al[7 - i] = 1
        gp.output(dac, al)
        sleep(.01)
        if gp.input(comp) == 1:
            al[i] = 0
    return(int("".join(al), base=2))


try:
    while True:
        v = adc()
        if v == 0:
            continue
        gp.output(dac, int_to_bin(v))
        print(f"{v}, {(3.3/256)*v} V")
        time.sleep(1)
     

finally:
    gp.output(dac, 0)
    gp.cleanup()