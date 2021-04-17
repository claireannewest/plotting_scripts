import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

data = np.loadtxt('Spectrum_tetra')
data_sort = data[data[:,0].argsort(),]
wave = 1.240/data_sort[:,0]
EEL = data_sort[:,2]
plt.plot(wave, EEL,label='tetra')

data = np.loadtxt('Spectrum_tri')
data_sort = data[data[:,0].argsort(),]
wave = 1.240/data_sort[:,0]
EEL = data_sort[:,2]
plt.plot(wave, EEL, label='trimer')
plt.legend()
plt.show()

