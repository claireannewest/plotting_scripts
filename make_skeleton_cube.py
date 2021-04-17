import numpy as np
import matplotlib.pyplot as plt
import argparse 
from mpl_toolkits.mplot3d import Axes3D

lat_space = 1 # nm per every lattice site
side = int(30/lat_space) # side length (needs to be even)
shell = int(4/lat_space) # shell / 2 = thickness of shell (needs to even)
curve = 4 # defines curvature of the cube and shell.
tune_thickness = 3 # quanitity which shaves off more or less of the shell on each face

def make_shape(core_too):
	'''Makes the shape points by carving out regions of space.'''
	if side % 2 != 0: print('ERROR: The variable "side" needs to be even.'); exit()
	if shell % 2 != 0: print('ERROR: The variable "shell" needs to be even.'); exit()

	# Define x,y,z _range to be larger than the size of your shape,
	# you'll carve out from these points which ones you want.
	x_range = np.linspace(-(side+shell)/2-2, (side+shell)/2+2, (side+shell)+5) 
	y_range = np.linspace(-(side+shell)/2-2, (side+shell)/2+2, (side+shell)+5) 
	z_range = np.linspace(-(side+shell)/2-2, (side+shell)/2+2, (side+shell)+5) 

	# Turn the 1D arrays into 3D grids
	xgrid, ygrid, zgrid = np.meshgrid(x_range, y_range, z_range) 
	# Restack the 3 3D grids into 3 1D arrays
	all_points = np.column_stack((np.ravel(xgrid), np.ravel(ygrid), np.ravel(zgrid))) 
	# Initialize a bunch of arrays (you have to do this because
	# you don't know how many entries your arrays will need.)
	Xval = []; Yval = []; Zval = [];
	Xval_skel = []; Yval_skel = []; Zval_skel = [];

	for row in range(0, len(all_points[:,0])):
		x = all_points[row, 0]
		y = all_points[row, 1]
		z = all_points[row, 2]
		A = side/(2)+1 # used to calculate the curavature of the underlying cube
		A_skel = (side+shell)/(2)+1 # used to calculate the curavature of the skeleton 
		A_remove = A - tune_thickness # this will make the skeleton thicker or thinner
		if np.abs(x/A)**curve + np.abs(y/A)**curve + np.abs(z/A)**curve  < 1 : 
			# Check if the x, y, z point should be a core square point
			# If so, add this point to the arrays
			Xval = np.append(Xval, x)
			Yval = np.append(Yval, y) 
			Zval = np.append(Zval, z) 
		elif np.abs(x/A_skel)**curve + np.abs(y/A_skel)**curve + np.abs(z/A_skel)**curve  < 1:
			# If you're not in the core cube, but you are in the region of the outer shell, continue
			if (
				# Now we have a uniform cube shell, but we want the faces of the shell removed. So  
				# next I create a bunch of cubes centered on each of the eight faces. If you're outside 
				# this new cube, then you're a skeleton point.
				(np.abs(x/A_remove)**curve + np.abs((y+A)/A_remove)**curve + np.abs(z/A_remove)**curve >= 1) &\
				(np.abs(x/A_remove)**curve + np.abs((y-A)/A_remove)**curve + np.abs(z/A_remove)**curve >= 1) &\
				(np.abs(x/A_remove)**curve + np.abs(y/A_remove)**curve + np.abs((z+A)/A_remove)**curve >= 1) &\
				(np.abs(x/A_remove)**curve + np.abs(y/A_remove)**curve + np.abs((z-A)/A_remove)**curve >= 1) &\
				(np.abs((x+A)/A_remove)**curve + np.abs(y/A_remove)**curve + np.abs(z/A_remove)**curve  >= 1) &\
				(np.abs((x-A)/A_remove)**curve + np.abs(y/A_remove)**curve + np.abs(z/A_remove)**curve  >= 1) \
				):
				Xval_skel = np.append(Xval_skel, x)
				Yval_skel = np.append(Yval_skel, y)
				Zval_skel = np.append(Zval_skel, z)

	# If you want to save the core and the skeleton, or if you just want the skeleton.
	if core_too == True:
		all_xpoints = np.hstack((Xval, Xval_skel))
		all_ypoints = np.hstack((Yval, Yval_skel))
		all_zpoints = np.hstack((Zval, Zval_skel))
		ICOMP_core = np.zeros(len(Xval))+1
		ICOMP_skel = np.zeros(len(Xval_skel))+2
		all_ICOMP = np.hstack((ICOMP_core, ICOMP_skel))
	if core_too == False:
		all_xpoints = Xval_skel
		all_ypoints = Yval_skel
		all_zpoints = Zval_skel
		all_ICOMP = np.zeros(len(Xval_skel))+1

	return all_xpoints, all_ypoints, all_zpoints, all_ICOMP

def write_shapefile():
	''' This function writes the N rods to a shape file '''
	x, y, z, ICOMP = make_shape(core_too=False)
	N = len(x)
	file = open(str('shape.dat'),'w')
	file.write(str(' Cube Skeleton Shape') + '\n')
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

# write_shapefile()

def plot_shape_file(dim):
	x, y, z, ICOMP = make_shape(core_too=True)

	if dim == 2:
		fig = plt.figure(figsize=(3,5))
		ax1 = fig.add_subplot(311)
		idx1 = np.where((ICOMP==1) & (x==0))
		ax1.scatter(y[idx1], z[idx1], c='red',alpha=.2)
		idx1 = np.where((ICOMP==2) & (x==0))
		ax1.scatter(y[idx1], z[idx1], marker='+',c='blue')

		ax2 = fig.add_subplot(312)
		idx1 = np.where((ICOMP==1))
		ax2.scatter(y[idx1], z[idx1], c='red',alpha=.2)
		idx1 = np.where((ICOMP==2) & (x == max(x)))
		ax2.scatter(y[idx1], z[idx1], marker='+',c='blue')
		ax1.axis('equal')

	if dim == 3:
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		idx1 = np.where((ICOMP==1))
		ax.scatter(x[idx1], y[idx1], z[idx1],marker='o', c='red',alpha=.2)
		idx2 = np.where((ICOMP==2))
		ax.scatter(x[idx2], y[idx2], z[idx2], marker='+',c='blue')
		ax.grid(False)
		ax.set_xlabel('x')
		ax.set_ylabel('y')
		ax.set_zlabel('z')


	print('Full shape dimensions (in DS)')
	print('x', min(x), max(x))
	print('y', min(y), max(y))
	print('z', min(z), max(z))
	plt.axis('equal')
	plt.show()

plot_shape_file(dim=3)




