import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt
import sys
from decimal import Decimal
import math
from scipy.special import kn

e = 4.80326E-10 #statC
c = 2.998E+10 #cm/s
hbar_eVs = 6.58212E-16 #eV*s
hbar_cgs = 1.0545716E-27 # cm^2*g/s

w0 = 1.3/hbar_eVs
magR = 10E-7
v = 0.48

gamNR = 0.07/hbar_eVs

def alpha(w):
	m = 1E-32
	gam = gamNR + w**2*(2.0*e**2)/(3.0*m*c**3)
	return e**2/m * 1/(-w**2 - 1j*w*gam + w0**2)

def gamEEL(w):
	gamL = 1/np.sqrt(1-v**2)
	constants = 4.0*e**2/((hbar_eVs)*hbar_cgs*np.pi*(v*c)**4*gamL**2)*(w)**2*(kn(1,w*magR/(v*c*gamL)))**2
	return constants*np.imag(alpha(w=w))

w = np.linspace(1/hbar_eVs, 2/hbar_eVs, 300)




w_eig = np.sqrt(-gamNR**2/4+w0**2)
print w_eig*hbar_eVs
print w[np.where(gamEEL(w=w) == max(gamEEL(w=w)))]*hbar_eVs



plt.plot(w*hbar_eVs, gamEEL(w=w))
plt.show()