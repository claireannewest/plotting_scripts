import numpy as np
import matplotlib.pyplot as plt

def temp_2d(xplane, DS):
	"""Makes a 2D colormap of the temperature.

	Keywords:
	xplane -- x-slice of the 2D image [DS]
	DS -- dipole spacing 
	"""
	temp_data = np.loadtxt('temp.out')
	idx = np.where(temp_data[:,0] == xplane)
	y = temp_data[idx,1][0]*DS
	z = temp_data[idx,2][0]*DS
	T = temp_data[idx,3][0]
	idx_sort = np.lexsort((y, z))
	new_y = y[idx_sort]
	new_z = z[idx_sort]
	new_temps = T[idx_sort]
	y_wind = int(max(y/DS) - min(y/DS) + 1); z_wind = int(max(z/DS) - min(z/DS) + 1)
	temp_grid = new_temps.reshape(z_wind, y_wind, order='c')
	plt.imshow(temp_grid,origin='lower',cmap='inferno')
	plt.xlabel('y [nm]')
	plt.ylabel('z [nm]')
	plt.colorbar(label='$\Delta$ T [ $\circ$ C]')
	plt.show()

# temp_2d(xplane=-6, DS=1)

def temp_1d(xplane, zplane, DS):
	temp_data = np.loadtxt('temp.out')
	idx = np.where((temp_data[:,0] == xplane) & (temp_data[:,2] == zplane ))
	x = temp_data[idx,0][0]*DS
	y = temp_data[idx,1][0]*DS
	z = temp_data[idx,2][0]*DS
	T = temp_data[idx,3][0]
	plt.scatter(y, T)
	plt.xlabel('y [nm]')
	plt.ylabel('$\Delta$ T [ $\circ$ C]')
	plt.show()


# temp_1d(xplane=-11, zplane=0, DS=1)