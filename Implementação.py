import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import noisereduce as nr

a = 0
seg = 0
vol = 0
cur = 0
Vmax = 0
Imax = 0
Vmin = 300
Imin = 300
picos = 0

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

'''------------------------------------------------------------------------'''

for i in range(0, 120000):
    
