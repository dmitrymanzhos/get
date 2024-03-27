import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setup(dac, gp.OUT, initial=gp.HIGH)

def int_to_bin(a):
    return [int(i) for i in bin(a)[2:].rjust(8, '0')]
    

try:
    t = float(input())
    while True:
        for i in range(0, 255):
            gp.output(dac, int_to_bin(i))
            time.sleep(t)
        for i in range (255, -1, -1):
            gp.output(dac, int_to_bin(i))
            time.sleep(t)

except KeyboardInterrupt:
    print()
    pass


finally:
    gp.output(dac, 0)
    gp.cleanup()