import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.patches import Rectangle
from matplotlib import rcParams
from scipy import interpolate
from scipy.interpolate import interp2d 
from mpl_toolkits.axes_grid1 import make_axes_locatable

rcParams.update({'figure.autolayout': True})
plt.rc('text', usetex=True)
plt.rc('font', family='serif') 

####################
###### Chubby ######
####################

### E in plane, B in plane
# folder = 'pw/pw_chubbie'
# kind = '0deg'
# energy = '1.89'
# which='imag' #bfield=real

### E in plane 45, B in plane 45
# folder = 'pw/pw_chubbie'
# kind = '45pol0deg'
# energy = '1.89'
# which='real'
# which='imag'#efield

### E in plane, B out of plane
# folder = 'pw/pw_chubbie'
# kind = '90deg'
# energy = '1.92' #'1.92'
# which='imag'
#which='real' # efield

# ### E in plane 45, B out of plane 45
# folder = 'pw/pw_chubbie'
# kind = 'elong_45pol90deg'
# energy = '1.72'#'1.36'
# which='real'

###################
#### Elongated ####
###################

### E in plane, B in plane
folder = 'pw/pw_elongate'
kind = 'elong_0deg'
energy = '1.67'
which='mag'

### E in plane 45, B in plane 45
folder = 'pw/pw_elongate'
kind = 'elong_45pol0deg'
energy = '1.67'
which='mag'

### E in plane, B out of plane
# folder = 'pw/pw_elongate'
# kind = 'elong_90deg'
# energy = '1.72'#'1.72'#1.36'
# which='mag'

### E in plane 45, B out of plane 45
# folder = 'pw/pw_elongate'
# kind = 'elong_45pol90deg'
# energy = '1.36'
# which='imag'



def seeEField(which):
	file = str(folder)+str('/field_')+str(kind)+str('_')+str(energy)+str('eV')
	data = np.loadtxt(file,skiprows=23)
	x = data[:,0]; y = data[:,1]; z = data[:,2]
	Ex_real = data[:,3]; Ex_imag = data[:,4]
	Ey_real = data[:,5]; Ey_imag = data[:,6]
	Ez_real = data[:,7]; Ez_imag = data[:,8]
	data = np.loadtxt(file,skiprows=23)
	x = data[:,0]; y = data[:,1]; z = data[:,2]
	Ex_real = data[:,3]; Ex_imag = data[:,4]
	Ey_real = data[:,5]; Ey_imag = data[:,6]
	Ez_real = data[:,7]; Ez_imag = data[:,8]
	fig = plt.figure(1, figsize=[2,2])
	ax = plt.gca()
	ax.set_aspect('equal', adjustable='box')

	if kind == '' or kind == 'elongtetra' or kind == '0deg' or kind == '45pol0deg' or kind =='elong_0deg' or kind == 'elong_45pol0deg' or kind == 'elong_monolong':
		if which == 'real': Eplot = Ex_real
		if which == 'imag': Eplot = Ex_imag
		if which == 'mag': Eplot = np.sqrt(Ex_real**2+Ex_imag**2+Ey_real**2+Ey_imag**2+Ez_real**2+Ez_imag**2)

		if which == 'real' or which == 'imag':
			plt.scatter(y,z,c=Eplot,s=50,cmap='seismic',vmin=-max(Eplot)*.4,vmax=max(Eplot)*.4)
			divider = make_axes_locatable(ax)
			cax = divider.append_axes("right", size="5%", pad=0.05)
			plt.clim([-max(Eplot), max(Eplot)])
			plt.colorbar(ticks=np.linspace(-max(Eplot), max(Eplot), 3),cax=cax)
			plt.xticks([]); plt.yticks([])

		if which == 'mag':
			plt.scatter(y,z,c=Eplot,s=50,cmap='viridis',vmin=0,vmax=max(Eplot)*.4)
			divider = make_axes_locatable(ax)
			cax = divider.append_axes("right", size="5%", pad=0.05)
			plt.clim([0, max(Eplot)])
			plt.colorbar(ticks=np.linspace(0, max(Eplot), 3),cax=cax)
			plt.xticks([]); plt.yticks([])

	if kind == '90deg' or kind =='45pol90deg' or kind == 'elong_90deg' or kind == 'elong_45pol90deg':
		if which == 'real': Eplot = Ez_real
		if which == 'imag': Eplot = Ez_imag
		if which == 'mag': Eplot = np.sqrt(Ex_real**2+Ex_imag**2+Ey_real**2+Ey_imag**2+Ez_real**2+Ez_imag**2)

		if which == 'real' or which == 'imag':
			plt.scatter(x,y,c=Eplot,s=50,cmap='seismic', vmin=-max(Eplot)*.4,vmax=max(Eplot)*.4)
			divider = make_axes_locatable(ax)
			cax = divider.append_axes("right", size="5%", pad=0.05)
			plt.clim([-max(Eplot), max(Eplot)])
			plt.colorbar(ticks=np.linspace(-max(Eplot), max(Eplot), 3),cax=cax)
			plt.xticks([]); plt.yticks([])

		if which == 'mag':
			plt.scatter(x,y,c=Eplot,s=50,cmap='viridis',vmin=0,vmax=max(Eplot)*.4)
			divider = make_axes_locatable(ax)
			cax = divider.append_axes("right", size="5%", pad=0.05)
			plt.clim([0, max(Eplot)])
			plt.colorbar(ticks=np.linspace(0, max(Eplot), 3),cax=cax)
			plt.xticks([]); plt.yticks([])
	plt.show()

seeEField(which=which)

###############################################################################################################
###############################################################################################################

def seeBField(which):
	file = str(folder)+str('/bfield_')+str(kind)+str('_')+str(energy)+str('eV')
	data = np.loadtxt(file,skiprows=23)
	x = data[:,0]; y = data[:,1]; z = data[:,2]
	Bx_real = data[:,3]; Bx_imag = data[:,4]
	By_real = data[:,5]; By_imag = data[:,6]
	Bz_real = data[:,7]; Bz_imag = data[:,8]
	fig = plt.figure(1, figsize=[2,2])
	ax = plt.gca()
	ax.set_aspect('equal', adjustable='box')
	plt.xticks([]); plt.yticks([])

	if kind == '' or kind == 'elongtetra' or kind == '0deg' or kind == '45pol0deg' or kind =='elong_0deg' or kind == 'elong_45pol0deg' or kind == 'elong_monolong':
		if which == 'real': Bplot = Bx_real
		if which == 'imag': Bplot = Bx_imag
		if which == 'mag': Bplot = np.sqrt(Bx_real**2+Bx_imag**2+By_real**2+By_imag**2+Bz_real**2+Bz_imag**2)

		if which == 'real' or which == 'imag':
			plt.scatter(y,z,c=Bplot,s=50,cmap='seismic',vmin=-max(Bplot)*.4,vmax=max(Bplot)*.4)
			divider = make_axes_locatable(ax)
			cax = divider.append_axes("right", size="5%", pad=0.05)
			plt.clim([-max(Bplot), max(Bplot)])
			plt.colorbar(ticks=np.linspace(-max(Bplot), max(Bplot), 3),cax=cax)

		if which == 'mag':
			plt.scatter(y,z,c=Bplot,s=50,cmap='viridis',vmin=0,vmax=max(Bplot)*.4)
			divider = make_axes_locatable(ax)
			cax = divider.append_axes("right", size="5%", pad=0.05)
			plt.clim([0, max(Bplot)])
			plt.colorbar(ticks=np.linspace(0, max(Bplot), 3),cax=cax)

	if kind == '90deg' or kind =='45pol90deg' or kind == 'elong_90deg' or kind == 'elong_45pol90deg':
		if which == 'real': Bplot = Bz_real
		if which == 'imag': Bplot = Bz_imag
		if which == 'mag': Bplot = np.sqrt(Bx_real**2+Bx_imag**2+By_real**2+By_imag**2+Bz_real**2+Bz_imag**2)

		if which == 'real' or which == 'imag':
			plt.scatter(x,y,c=Bplot,s=50,cmap='seismic', vmin=-max(Bplot)*.4,vmax=max(Bplot)*.4)
			divider = make_axes_locatable(ax)
			cax = divider.append_axes("right", size="5%", pad=0.05)
			plt.clim([-max(Bplot), max(Bplot)])
			plt.colorbar(ticks=np.linspace(-max(Bplot), max(Bplot), 3),cax=cax)

		if which == 'mag':
			plt.scatter(x,y,c=Bplot,s=50,cmap='viridis',vmin=0,vmax=max(Bplot)*.4)
			divider = make_axes_locatable(ax)
			cax = divider.append_axes("right", size="5%", pad=0.05)
			plt.clim([0, max(Bplot)])
			plt.colorbar(ticks=np.linspace(0, max(Bplot), 3),cax=cax)

	plt.show()
#seeBField(which=which)

