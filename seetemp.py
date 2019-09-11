import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('temp.out')
x_plane = 0
z_plane = 0
data_sortx = np.where(data[:,0] == x_plane)
data_sort = data[data_sortx]

data_sortz = np.where(data_sort[:,2] == z_plane)
data_sorted = data_sort[data_sortz]


data_sort_post = data_sorted[data_sorted[:,1].argsort(),]

y = data_sort_post[:,1]
T = data_sort_post[:,3]
plt.plot(y,T)
plt.show()