import numpy as np
import matplotlib.pyplot as plt


fig, (ax1, ax2) = plt.subplots(2,1)

data = np.loadtxt(str('rod/shape.dat_withoutshell'), skiprows=7)
DS = 2
x = data[:,1]*DS
y = data[:,2]*DS
z = data[:,3]*DS
ICOMP = data[:,4]
midpoint = (min(x)-max(x))/2+max(x)

idx1 = np.where((ICOMP==1) & (x==midpoint))
ax1.scatter(y[idx1], z[idx1], c='red',alpha=.2)

idx2 = np.where((ICOMP==2) & (x==midpoint))
ax1.scatter(y[idx2], z[idx2], marker='+',c='blue')
ax1.set_xlabel('y [nm]')
ax1.set_ylabel('z [nm]')
ax1.axis('equal')

data = np.loadtxt(str('rod/shape.dat_withshell'), skiprows=7)
DS = 2
x = data[:,1]*DS
y = data[:,2]*DS
z = data[:,3]*DS
ICOMP = data[:,4]
midpoint = (min(x)-max(x))/2+max(x)

idx1 = np.where((ICOMP==1) & (x==midpoint))
ax2.scatter(y[idx1], z[idx1], c='red',alpha=.2)

idx2 = np.where((ICOMP==2) & (x==midpoint))
ax2.scatter(y[idx2], z[idx2], marker='+',c='blue')
ax2.set_xlabel('y [nm]')
ax2.set_ylabel('z [nm]')
ax2.axis('equal')


plt.subplots_adjust(hspace=.3)
plt.show()
