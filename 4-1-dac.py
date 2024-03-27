import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setup(dac, gp.OUT, initial=gp.HIGH)


def int_to_bin(a):
    return [int(i) for i in bin(a)[2:].rjust(8, '0')]
    

try:
    while True:
        a = int_to_bin(int(input()))
        gp.output(dac, a)
        print(int("".join([str(i) for i in a]), 2)*(3.3/256), ' V')


except KeyboardInterrupt:
    print()
    pass

except Exception:
    print("Invalid Input")
    pass



finally:
    gp.output(dac, 0)
    gp.cleanup()