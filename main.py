from NSG.generator import Generator
from random import randint
from utils.utils import *
import numpy as np
import matplotlib.pyplot as plt

HIGH_VALUE = 4294967296
LOW_VALUE = 0

size = 2501
array = list()
suma = 0
for i in range(100):
        rand_list = [randint(LOW_VALUE,HIGH_VALUE),randint(LOW_VALUE,HIGH_VALUE),
                randint(LOW_VALUE,HIGH_VALUE),randint(LOW_VALUE,HIGH_VALUE),randint(1,HIGH_VALUE+1)]
        gen = Generator(rand_list[0],rand_list[1],rand_list[2],rand_list[3],rand_list[4]) 
        try:
                array = normalize(gen.generate_list(size))
        except ZeroDivisionError:
                print("!!!!ZERO!!!!!!!")
                print(array)
        T = find_T(array[int(size*0.2):size])
        M = sum(array)/(size)
        new_array = list((i - M)**2 for i in array)
        D = sum(new_array)/size
        S_b_T = sequence_bit_test(array)
        s = squeeze_test(array)

        fig = plt.figure()
        fig.set_size_inches(15,10)
        ax1 = fig.add_subplot(131)
        ax1.hist(array,500)
        ax2 = fig.add_subplot(132)
        ax2.hist(s)
        ax3 = fig.add_subplot(133)
        ax3 = ax3.imshow(np.array(array).reshape(50,50))

        fig.add_subplot(ax1)
        # if is_good_sequence(0,T,HIGH_VALUE,M,D,S_b_T):
        # print(array)
        # print(f'T:{T}')
        # print(f'M:{M}')
        # print(f'D:{D}')
        # print(f'S_b_T:{S_b_T}')
        # wirte_to_file(rand_list)
        fig.suptitle(f"Rand List:{rand_list}\nT: {T}\nM: {M}\nD: {D}\nS_b_T: {S_b_T}")
        fig.savefig(f"fig/{i}_hist.png")


        # plt.savefig(f"fig/{i}_diag.png")
        # plt.close()
        # if i%100 == 0:
        #         print('RUNNUNG...')