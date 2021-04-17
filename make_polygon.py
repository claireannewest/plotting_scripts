import numpy as np
import matplotlib.pyplot as plt
import argparse 

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

	x_range = np.linspace(-thick/2-10, thick/2+10, thick+21) # this array should be large enough to span the space of x coord
	y_range = np.linspace(-length/2, length/2, length+21) # this array should be large enough to contain any rotation angle of the rod
	z_range = np.linspace(-length/2, length/2, length+21) # this array should be large enough to contain any rotation angle of the rod

	xgrid, ygrid, zgrid = np.meshgrid(x_range, y_range, z_range) # turns the 1D arrays into 3D grids
	all_points = np.column_stack((np.ravel(xgrid), np.ravel(ygrid), np.ravel(zgrid))) # restacks the 3 3D grids into 3 1D arrays
	Xval = []; Yval = []; Zval = []

	for row in range(0, len(all_points[:,0])): #loops through each x, y, z coordinate
		x = all_points[row, 0]
		y = all_points[row, 1]
		z = all_points[row, 2]

		A = thick/(2*lat_space)+1 # used to calculate the curavature of the rod in x direction
		B = length/(2*lat_space)+1 # used to calculate the curavature of the rod in y direction
		C = width/(2*lat_space)+1 # used to calculate the curavature of the rod in z direction

		yp = y*np.cos(theta)-z*np.sin(theta) # rotated coordinates
		zp = y*np.sin(theta)+z*np.cos(theta) # rotated coordinates
		if np.abs((x/A))**r + (np.abs((yp/B))**r)**(t/r) + np.abs((zp/C))**t  < 1 : # checks if the x, y, z point should be a rod point
			y_shift = y + y_offset # shifts the y point after it's been rotated 
			z_shift = z + z_offset # shifts the z point after it's been rotated 
			Xval = np.append(Xval, x) # adds this point to the array which will be used to write the shape file
			Yval = np.append(Yval, y_shift) # adds this point to the array which will be used to write the shape file
			Zval = np.append(Zval, z_shift) # adds this point to the array which will be used to write the shape file
	return Xval, Yval, Zval

def plot_shape():
	''' This function collects each rod and plots it ''' 
	fig = plt.figure(num=None, figsize=(6, 6), dpi=80, facecolor='w', edgecolor='k')  
	right_xval, right_yval, right_zval = rotate_rod(theta=np.pi/3, 
										y_offset=0,
										z_offset=0)

	bottom_xval, bottom_yval, bottom_zval = rotate_rod(theta=0,
										y_offset=0,
										z_offset=0)

	left_xval, left_yval, left_zval = rotate_rod(theta=-np.pi/3, 
										y_offset=0,
										z_offset=0)

	plt.scatter(right_yval, right_zval)
	plt.scatter(bottom_yval, bottom_zval)
	plt.scatter(left_yval, left_zval)
	plt.axis('equal')
	plt.show()

plot_shape()

def write_shapefile():
	''' This function writes the N rods to a shape file '''
	right_xval, right_yval, right_zval = rotate_rod(theta=np.pi/3, 
									y_offset=0,
									z_offset=0)

	bottom_xval, bottom_yval, bottom_zval = rotate_rod(theta=0,
										y_offset=0,
										z_offset=0)

	left_xval, left_yval, left_zval = rotate_rod(theta=-np.pi/3, 
										y_offset=0,
										z_offset=0)
	all_xpoints = np.hstack((right_xval, bottom_xval, left_xval))
	all_ypoints = np.hstack((right_yval, bottom_yval, left_yval))
	all_zpoints = np.hstack((right_zval, bottom_zval, left_zval))
	all_shapepoints = np.column_stack((all_xpoints, all_ypoints, all_zpoints))

	file = open(str('shape.dat_trimer'),'w')
	file.write(str(' Trimer Shape') + '\n')
	file.write('\t' + str(len(all_shapepoints[:,0])) + str(' = number of dipoles in target') + '\n')
	file.write(str(' 1.000000 0.000000 0.000000 = A_1 vector') + '\n')
	file.write(str(' 0.000000 1.000000 0.000000 = A_2 vector') + '\n')
	file.write(str(' 1.000000 1.000000 1.000000 = (d_x,d_y,d_z)/d') + '\n')
	file.write(str(' 0.000000 0.000000 0.000000 = (x,y,z)/d') + '\n')
	file.write(str(' JA  IX  IY  IZ ICOMP(x,y,z)') + '\n')
	count = 0
	for j in range(0, len(all_shapepoints[:,0])):
		count = count+1
		x = all_shapepoints[j,0]
		y = all_shapepoints[j,1]
		z = all_shapepoints[j,2]
		file.write('\t' + str(count) + '\t' + str(int(x)) + '\t' + str(int(y)) + '\t' + str(int(z)) + '\t' + str(1) + '\t' + str(1) + '\t' + str(1) + '\n')
	file.close()	

# write_shapefile()



