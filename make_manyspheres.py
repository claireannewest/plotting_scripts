import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

lat_space = 1 # nm per every lattice site
radius = int(10/lat_space) # sphere radius 

def make_single_sphere(xshift, yshift, zshift):
	''' This function rotates and shifts a single rod ''' 
	x_range = np.linspace(-radius-2, radius+2, 2*radius+5)
	y_range = np.linspace(-radius-2, radius+2, 2*radius+5)
	z_range = np.linspace(-radius-2, radius+2, 2*radius+5)

	xgrid, ygrid, zgrid = np.meshgrid(x_range, y_range, z_range) # Turns the 1D arrays into 3D grids
	all_points = np.column_stack((np.ravel(xgrid), np.ravel(ygrid), np.ravel(zgrid))) # Restacks the 3 3D grids into 3 1D arrays
	Xval = []; Yval = []; Zval = [];
	for row in range(0, len(all_points[:,0])): 
		# Loops through each x, y, z coordinate
		x = all_points[row, 0]
		y = all_points[row, 1]
		z = all_points[row, 2]
		if x**2 + y**2 + z**2  <= radius**2 : # checks if the x, y, z point should be a sphere point
			# Adds this point to the array which will be used to write the shape file and shift it
			Xval = np.append(Xval, x+xshift) 
			Yval = np.append(Yval, y+yshift) 
			Zval = np.append(Zval, z+zshift)
	ICOMP = np.zeros(len(Xval))+1
	return Xval, Yval, Zval, ICOMP	

def make_multiple_spheres(ifplot):
	shift = 20
	x_1, y_1, z_1, ICOMP_1 = make_single_sphere(xshift=-shift, yshift=-shift, zshift=-shift)
	x_2, y_2, z_2, ICOMP_2 = make_single_sphere(xshift=shift, yshift=-shift, zshift=-shift)
	x_3, y_3, z_3, ICOMP_3 = make_single_sphere(xshift=shift, yshift=shift, zshift=-shift)
	x_4, y_4, z_4, ICOMP_4 = make_single_sphere(xshift=shift, yshift=-shift, zshift=shift)
	x_5, y_5, z_5, ICOMP_5 = make_single_sphere(xshift=-shift, yshift=shift, zshift=shift)
	x_6, y_6, z_6, ICOMP_6 = make_single_sphere(xshift=-shift, yshift=shift, zshift=-shift)
	x_7, y_7, z_7, ICOMP_7 = make_single_sphere(xshift=-shift, yshift=-shift, zshift=shift)
	x_8, y_8, z_8, ICOMP_8 = make_single_sphere(xshift=shift, yshift=shift, zshift=shift)

	all_x = np.hstack((x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8))
	all_y = np.hstack((y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8))
	all_z = np.hstack((z_1, z_2, z_3, z_4, z_5, z_6, z_7, z_8))
	all_ICOMP = np.hstack((ICOMP_1, ICOMP_2, ICOMP_3, ICOMP_4, ICOMP_5, ICOMP_6, ICOMP_7, ICOMP_8))
	if ifplot == True:
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.scatter(all_x, all_y, all_z,marker='o', c='red')
		ax.grid(False)
		ax.set_xlabel('x')
		ax.set_ylabel('y')
		ax.set_zlabel('z')
		plt.show()
	return all_x, all_y, all_z, all_ICOMP

make_multiple_spheres(ifplot=True)


def write_shapefile():
	''' This function writes the N rods to a shape file '''
	x, y, z, ICOMP = make_multiple_spheres(ifplot=False)
	N = len(x)
	file = open(str('shape.dat'),'w')
	file.write(str(' Spheres Shape') + '\n')
	file.write('\t' + str(N) + str(' = number of dipoles in target') + '\n')
	file.write(str(' 1.000000 0.000000 0.000000 = A_1 vector') + '\n')
	file.write(str(' 0.000000 1.000000 0.000000 = A_2 vector') + '\n')
	file.write(str(' 1.000000 1.000000 1.000000 = (d_x,d_y,d_z)/d') + '\n')
	file.write(str(' 0.000000 0.000000 0.000000 = (x,y,z)/d') + '\n')
	file.write(str(' JA  IX  IY  IZ ICOMP(x,y,z)') + '\n')
	count = 0
	for j in range(0, N):
		count = count+1
		file.write('\t' + str(count) + '\t' + str(int(x[j])) + '\t' + str(int(y[j])) + '\t' + str(int(z[j])) + '\t' + str(ICOMP[j]) + '\t' + str(ICOMP[j]) + '\t' + str(ICOMP[j]) + '\n')
	file.close()	

write_shapefile()






