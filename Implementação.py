import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics
import scipy

a = 0
seg = 0
vol = 0
cur = 0
Vmax = 0
Imax = 0
Vmin = 300
Imin = 300
picos = 0
Vrms = 0
Irms = 0

intervalo = np.zeros(120000)
datarmsv = np.zeros(120000)
datarmsi = np.zeros(120000)
peak = np.zeros(120000)
# dataset[coluna][linha]
data = pd.read_csv("medidas_tempo_tensao_corrente.txt", sep="\s+", header=None)
tempo = data[0][119999]

for i in range(0, 119999):
    intervalo[i] = data[0][i + 1] - data[0][i]

for i in range(0, 120000):
    vol = vol + data[1][i]
    cur = cur + data[2][i]

print("Tensão média:", vol / 120000, "Volts")
print("Corrente média:", cur / 120000, "Amperes")
 
for i in range(0, 120000):
    if Vmax < abs(data[1][i]):
        Vmax = abs(data[1][i])
    else:
        Vmax = Vmax

for i in range(0, 120000):
    if Imax < abs(data[2][i]):
        Imax = abs(data[2][i])
    else:
        Imax = Imax

for i in range(0, 120000):
    if Imin > abs(data[2][i]):
        Imin = abs(data[2][i])
    else:
        Imin = Imin

for i in range(0, 120000):
    if Vmin > abs(data[1][i]):
        Vmin = abs(data[1][i])
    else:
        Vmin = Vmin

for i in range(0, 120000):
    datarmsv[i] = data[1][i] / math.sqrt(2)
    datarmsi[i] = data[2][i] / math.sqrt(2)

for i in range(0, 119999):
    if data[1][i] > 0 and data[1][i + 1] < 0:
        picos = picos + 1

periodo = tempo / picos
freq = 1 / periodo

for i in range(0, 120000):
   Vrms = Vrms + pow(data[1][i], 2)
   Irms = Irms + pow(data[2][i], 2)
Vrms = math.sqrt(Vrms/(120000))
Irms = math.sqrt(Irms/(120000))
'''-------------------------------------------------------------------------'''
datav = np.zeros(50)
datai = np.zeros(50)
stdatav = np.zeros(50)
stdatai = np.zeros(50)

for i in range(0, 120000):
        if i < 2401:
            datav[0] = datav[0]+datarmsv[i]
            datai[0] = datai[0]+datarmsi[i]
        elif(i < 4801):
            datav[1] = datav[1]+datarmsv[i]
            datai[1] = datai[1]+datarmsi[i]
        elif i < 7201:
            datav[2] = datav[2]+datarmsv[i]
            datai[2] = datai[2]+datarmsi[i]
        elif i < 9601:
            datav[3] = datav[3]+datarmsv[i]
            datai[3] = datai[3]+datarmsi[i]
        elif i < 12001:
            datav[4] = datav[4]+datarmsv[i]
            datai[4] = datai[4]+datarmsi[i]
        elif i < 14401:
            datav[5] = datav[5]+datarmsv[i]
            datai[5] = datai[5]+datarmsi[i]
        elif i < 16801:
            datav[6] = datav[6]+datarmsv[i]
            datai[6] = datai[6]+datarmsi[i]
        elif i < 19201:
            datav[7] = datav[7]+datarmsv[i]
            datai[7] = datai[7]+datarmsi[i]
        elif i < 21601:
            datav[8] = datav[8]+datarmsv[i]
            datai[8] = datai[8]+datarmsi[i]
        elif i < 24001:
            datav[9] = datav[9]+datarmsv[i]
            datai[9] = datai[9]+datarmsi[i]
        elif i < 26401:
            datav[10] = datav[10]+datarmsv[i]
            datai[10] = datai[10]+datarmsi[i]
        elif i < 28801:
            datav[11] = datav[11]+datarmsv[i]
            datai[11] = datai[11]+datarmsi[i]
        elif i < 31201:
            datav[12] = datav[12]+datarmsv[i]
            datai[12] = datai[12]+datarmsi[i]
        elif i < 33601:
            datav[13] = datav[13]+datarmsv[i]
            datai[13] = datai[13]+datarmsi[i]
        elif i < 36001:
            datav[14] = datav[14]+datarmsv[i]
            datai[14] = datai[14]+datarmsi[i]
        elif i < 38401:
            datav[15] = datav[15]+datarmsv[i]
            datai[15] = datai[15]+datarmsi[i]
        elif i < 40801:
            datav[16] = datav[16]+datarmsv[i]
            datai[16] = datai[16]+datarmsi[i]
        elif i < 43201:
            datav[17] = datav[17]+datarmsv[i]
            datai[17] = datai[17]+datarmsi[i]
        elif i < 45601:
            datav[18] = datav[18]+datarmsv[i]
            datai[18] = datai[18]+datarmsi[i]
        elif i < 48001:
               datav[19] = datav[19]+datarmsv[i]
               datai[19] = datai[19]+datarmsi[i]
        elif i < 50401:
            datav[20] = datav[20]+datarmsv[i]
            datai[20] = datai[20]+datarmsi[i]
        elif i < 52801:
            datav[21] = datav[21]+datarmsv[i]
            datai[21] = datai[21]+datarmsi[i]
        elif i < 55201:
            datav[22] = datav[22]+datarmsv[i]
            datai[22] = datai[22]+datarmsi[i]
        elif i < 57601:
            datav[23] = datav[23]+datarmsv[i]
            datai[23] = datai[23]+datarmsi[i]
        elif i < 60001:
            datav[24] = datav[24]+datarmsv[i]
            datai[24] = datai[24]+datarmsi[i]
        elif i < 62401:
            datav[25] = datav[25]+datarmsv[i]
            datai[25] = datai[25]+datarmsi[i]
        elif i < 64801:
            datav[26] = datav[26]+datarmsv[i]
            datai[26] = datai[26]+datarmsi[i]
        elif i < 67201:
            datav[27] = datav[27]+datarmsv[i]
            datai[27] = datai[27]+datarmsi[i]
        elif i < 69601:
            datav[28] = datav[28]+datarmsv[i]
            datai[28] = datai[28]+datarmsi[i]
        elif i < 72001:
            datav[29] = datav[29]+datarmsv[i]
            datai[29] = datai[29]+datarmsi[i]
        elif i < 74401:
            datav[30] = datav[30]+datarmsv[i]
            datai[30] = datai[30]+datarmsi[i]
        elif i < 76801:
            datav[31] = datav[31]+datarmsv[i]
            datai[31] = datai[31]+datarmsi[i]
        elif i < 79201:
            datav[32] = datav[32]+datarmsv[i]
            datai[32] = datai[32]+datarmsi[i]
        elif i < 81601:
            datav[33] = datav[33]+datarmsv[i]
            datai[33] = datai[33]+datarmsi[i]
        elif i < 84001:
            datav[34] = datav[34]+datarmsv[i]
            datai[34] = datai[34]+datarmsi[i]
        elif i < 86401:
            datav[35] = datav[35]+datarmsv[i]
            datai[35] = datai[35]+datarmsi[i]
        elif i < 88801:
            datav[36] = datav[36]+datarmsv[i]
            datai[36] = datai[36]+datarmsi[i]
        elif i < 91201:
            datav[37] = datav[37]+datarmsv[i]
            datai[37] = datai[37]+datarmsi[i]
        elif i < 93601:
            datav[38] = datav[38]+datarmsv[i]
            datai[38] = datai[38]+datarmsi[i]
        elif i < 96001:
            datav[39] = datav[39]+datarmsv[i]
            datai[39] = datai[39]+datarmsi[i]
        elif i < 98401:
            datav[40] = datav[40]+datarmsv[i]
            datai[40] = datai[40]+datarmsi[i]
        elif i < 100801:
            datav[41] = datav[41]+datarmsv[i]
            datai[41] = datai[41]+datarmsi[i]
        elif i < 103201:
            datav[42] = datav[42]+datarmsv[i]
            datai[42] = datai[42]+datarmsi[i]
        elif i < 105601:
            datav[43] = datav[43]+datarmsv[i]
            datai[43] = datai[43]+datarmsi[i]
        elif i < 108001:
            datav[44] = datav[44]+datarmsv[i]
            datai[44] = datai[44]+datarmsi[i]
        elif i < 110401:
            datav[45] = datav[45]+datarmsv[i]
            datai[45] = datai[45]+datarmsi[i]
        elif i < 112801:
            datav[46] = datav[46]+datarmsv[i]
            datai[46] = datai[46]+datarmsi[i]
        elif i < 115201:
            datav[47] = datav[47]+datarmsv[i]
            datai[47] = datai[47]+datarmsi[i]
        elif i < 117601:
            datav[48] = datav[48]+datarmsv[i]
            datai[48] = datai[48]+datarmsi[i]
        elif i < 120001:
            datav[49] = datav[49]+datarmsv[i]
            datai[49] = datai[49]+datarmsi[i]
for i in range(0, 50):
    datav[i]=datav[i]/2400
    datai[i]=datai[i]/2400
stdatav = statistics.stdev(datav)
stdatai = statistics.stdev(datai)
histv = np.histogram(datav)
histi = np.histogram(datai)
normv = scipy.stats.normaltest(datav)
normi = scipy.stats.normaltest(datai)

'''------------------------------------------------------------------------'''

