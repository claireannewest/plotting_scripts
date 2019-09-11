import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
DS = 2
data = np.loadtxt('2nd_project/tri80_symm/psfs_2dscans/shape.dat',skiprows=23)
x= data[:,1]*DS
y= data[:,2]*DS
z= data[:,3]*DS


plt.scatter(y, z)
plt.axis('equal')
#plt.show()
print min(y)
