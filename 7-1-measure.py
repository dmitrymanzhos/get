import RPi.GPIO as gp
import time
import matplotlib.pyplot as plt
import numpy as np
import datetime

gp.setmode(gp.BCM)
gp.setwarnings(False)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

gp.setup(dac, gp.OUT, initial=gp.HIGH)
gp.setup(leds, gp.OUT, initial=gp.HIGH)
gp.setup(troyka, gp.OUT, initial=gp.HIGH)
gp.setup(comp, gp.IN)

def int_to_bin(a):
    return [int(i) for i in bin(a)[2:].rjust(8, '0')]

def adc():
    al = [0 for i in range(8)]
    for i in range(8):
        al[i] = 1
        gp.output(dac, al)
        time.sleep(.005)
        if gp.input(comp) == 1:
            al[i] = 0
    return(int("".join(al), base=2))


# try:
#     al = []
#     start_time = time.time()

try:
    time_start = time.time()
    count = 0
    data = []
    data1 = []
    time_list = []
    voltage = 0

    #Зарядка конденсатора
    print('Зарядка конденсатора')
    while voltage <= 206:
        voltage = adc()
        print(voltage)
        data1.append(voltage)
        data.append(voltage/256*3.3)
        time_list.append(time.time() - time_start)
        time.sleep(0)
        count+=1
        gp.output(leds, int_to_bin(voltage))

    gp.output(troyka, 0)

    #Разрядка конденсатора
    print('Разрядка конденсатора')
    while voltage >= 169:
        voltage = adc()
        print(voltage)
        data1.append(voltage)
        data.append(voltage/256*3.3)
        time_list.append(time.time() - time_start)
        time.sleep(0)
        count+=1
        gp.output(leds, int_to_bin(voltage))
    

    #Ищем полное время эксперимента
    time_end = time.time()
    time_total = time_end - time_start

    print('Графики')

    #Строим графики
    plt.plot(time_list, data)
    plt.xlabel("Время")
    plt.ylabel("Напряжение")
    plt.show()

    print('Запись в файл')

    #Запись в файл
    with open('data.txt', "w") as f:
        for i in data1:
            f.write(str(i) + '\n')

    with open('settings.txt', "w") as f:
        f.write('Частота дискретизации ' + str(1/time_total*count) + ' Гц ' + '\n')
        f.write('Шаг квантования 0.0129 В')

    print('Завершение программы')

finally:
    gp.output(leds, 0)
    gp.output(dac, 0)
    gp.cleanup()
    count = 0







finally:
    gp.output(dac, 0)
    gp.output(leds, 0)
    gp.cleanup()