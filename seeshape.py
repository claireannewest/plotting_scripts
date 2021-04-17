import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
data1 = np.loadtxt('shape.dat',skiprows=7)

JAval1 = data1[:,0]
x1 = data1[:,1]
y1 = data1[:,2]
z1 = data1[:,3]

array1 = np.column_stack((x1,y1,z1))
uni_array1 = np.unique(array1, axis=0)

new_x1 = uni_array1[:,0]
new_y1 = uni_array1[:,1]
new_z1 = uni_array1[:,2]

print('unique = ', uni_array1.shape)
print('all =', data1.shape)
plt.figure()
plt.scatter(y1, z1, color='black')
plt.figure()

plt.scatter(x1, z1)
plt.figure()

plt.scatter(y1, x1)
# plt.scatter(-150.0, 20.0)
plt.axis('equal')

plt.show()
print(min(x1), max(x1))
print(min(y1), max(y1))
print(min(z1), max(z1))

def check_Symmetric(data):
	y_quad = []
	z_quad = []

	y = data[:,2]
	z = data[:,3]
	for val in range(0, len(y)):
		if val > 0:
			y_quad = np.append(y, y_quad)
			z_quad = np.append(z, z_quad)

	plt.scatter(y_quad,z_quad)
	plt.show()


def zoomed_in():
	fig = plt.figure(num=None, figsize=(4, 9), dpi=80, facecolor='w', edgecolor='k')   
	ax = plt.subplot(2,1,1)
	plt.scatter(uni_array1[:,1], uni_array1[:,2])
	plt.plot(-81, 0,marker='x', color='black',mew=4,ms=10)
	plt.title('Rhombus, 0 deg')
	plt.xlim([-82,-72])
	plt.ylim([-5,5])
	ax.set_axisbelow(True)
	majorx_ticks = np.arange(-82, -72, 1)
	majory_ticks = np.arange(-5, 5, 1)
	ax.set_xticks(majorx_ticks)
	ax.set_yticks(majory_ticks)
	ax.grid(which='major')

	ax = plt.subplot(2,1,2)
	plt.scatter(uni_array2[:,1], uni_array2[:,2])
	plt.plot(0, -81, marker='x', color='black',mew=4,ms=10)
	plt.title('Rhombus, 90 deg')
	plt.xlim([-5,5])
	plt.ylim([-82,-72])
	ax.set_axisbelow(True)
	majorx_ticks = np.arange(-5, 5, 1)
	majory_ticks = np.arange(-82, -72, 1)
	ax.set_xticks(majorx_ticks)
	ax.set_yticks(majory_ticks)
	ax.grid(which='major')
	plt.show()

def rewrite_shape():
	file = open(str('shape.dat_0_DS1_new'),'w')
	file.write(str(' Rhombus Shape, 0 deg. DS=1') + '\n')
	file.write('\t' + str(int(len(new_z1))) + str(' = number of dipoles in target') + '\n')
	file.write(str(' 1.000000 0.000000 0.000000 = A_1 vector') + '\n')
	file.write(str(' 0.000000 1.000000 0.000000 = A_2 vector') + '\n')
	file.write(str(' ') + str(dx_on_d) + str(' ') + str(dy_on_d) + str(' ')  + str(dz_on_d) + str(' ') + str('= (d_x,d_y,d_z)/d') + '\n')
	file.write(str(' 0.000000 0.000000 0.000000 = (x,y,z)/d') + '\n')
	file.write(str(' JA  IX  IY  IZ ICOMP(x,y,z)') + '\n')
	for j in range(0, len(new_z1)):
		file.write('\t' + str(int(JAval1[j])) + '\t' + str(int(new_x1[j])) + '\t' + str(int(new_y1[j])) + '\t' + str(int(new_z1[j])) + '\t' + str(int(1)) + '\t' + str(int(1)) + '\t' + str(int(1)) + '\n')
	file.close()	


