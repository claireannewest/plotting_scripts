import numpy as np
import matplotlib.pyplot as plt

def rod_parameters(): 
	''' This function is where you input the parameters for a single rod '''
	lat_space = 2 # nm per every lattice site
	length = int(270/lat_space) # long axis
	width = int(37/lat_space) # short axis
	thick = int(15/lat_space) # propogation axis 
	r = 4 # defines curvature in x direction
	t = 4 # defines curvature in y, z direction (bigger = less curve)
	return length, width, thick, r, t, lat_space

def rotate_rod(theta, y_offset, z_offset):
	''' This function rotates and shifts a single rod ''' 
	length, width, thick, r, t, lat_space = rod_parameters()
	y_range = np.linspace(-length, length, 2*length+1) # this array should be large enough to contain any rotation angle of the rod
	z_range = np.linspace(-length/2, length/2, length+1) # this array should be large enough to contain any rotation angle of the rod
	print(y_range)
	ygrid, zgrid = np.meshgrid(y_range, z_range) # turns the 1D arrays into 3D grids
	all_points = np.column_stack((np.ravel(ygrid), np.ravel(zgrid))) # restacks the 3 3D grids into 3 1D arrays
	Yval = []; Zval = []

	for row in range(0, len(all_points[:,0])): #loops through each x, y, z coordinate
		y = all_points[row, 0]
		z = all_points[row, 1]

		B = length/(2*lat_space)+1 # used to calculate the curavature of the rod in y direction
		C = width/(2*lat_space)+1 # used to calculate the curavature of the rod in z direction

		yp = y*np.cos(theta)-z*np.sin(theta) # rotated coordinates
		zp = y*np.sin(theta)+z*np.cos(theta) # rotated coordinates
		if (np.abs((yp/B))**r)**(t/r) + np.abs((zp/C))**t  < 1 : # checks if the x, y, z point should be a rod point
			y_shift = y + y_offset # shifts the y point after it's been rotated 
			z_shift = z + z_offset # shifts the z point after it's been rotated 
			Yval = np.append(Yval, y_shift) # adds this point to the array which will be used to write the shape file
			Zval = np.append(Zval, z_shift) # adds this point to the array which will be used to write the shape file
	return Yval, Zval

right_yval, right_zval = rotate_rod(theta=np.pi/3, 
									y_offset=0,
									z_offset=0)

def plot_shape():
	''' This function collects each rod and plots it ''' 
	fig = plt.figure(num=None, figsize=(6, 6), dpi=80, facecolor='w', edgecolor='k')  
	right_yval, right_zval = rotate_rod(theta=np.pi/3, 
										y_offset=0,
										z_offset=0)

	bottom_yval, bottom_zval = rotate_rod(theta=0,
										y_offset=0,
										z_offset=0)

	left_yval, left_zval = rotate_rod(theta=-np.pi/3, 
										y_offset=0,
										z_offset=0)

	plt.scatter(right_yval, right_zval)
	plt.scatter(bottom_yval, bottom_zval)
	plt.scatter(left_yval, left_zval)
	plt.axis('equal')
	plt.show()

#plot_shape()
