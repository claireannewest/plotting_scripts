import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('ddfield.E')
x_plane = -14

data_sortx = np.where(data[:,0] == x_plane)
data_sort = data[data_sortx]
data_sort_post = data_sorted[data_sorted[:,1].argsort(),]
data_sort_post = data_sorted[data_sorted[:,2].argsort(),]

y = data_sort_post[:,1]
z = data_sort_post[:,2]
Ex_real = data_sort_post[:,3]
y_size = max(y)-min(y)+1
z_size = max(z)-min(z)+1


plt.plot(y,T)
plt.show()