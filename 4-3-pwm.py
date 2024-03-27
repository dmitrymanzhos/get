import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setwarnings(False)

out = 24
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setup(dac, gp.OUT, initial=gp.HIGH)
gp.setup(out, gp.OUT)
p = gp.PWM(24, 1000)
p.start(0)


def int_to_bin(a):
    return [int(i) for i in bin(a)[2:].rjust(8, '0')]
    
try:
    while True:
        a = float(input())
        p.ChangeDutyCycle(a)


except KeyboardInterrupt:
    print()
    pass


finally:
    p.stop()
    gp.output(dac, 0)
    gp.cleanup()