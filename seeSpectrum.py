import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('rod/Spectrum_n1.0_withoutshell')
data_sort = data[data[:,1].argsort(),]
aeff = data_sort[:,0]
wave = 1.240/data_sort[:,1]
C_ext = data_sort[:,2]*np.pi*aeff**2
C_abs = data_sort[:,3]*np.pi*aeff**2
C_sca = data_sort[:,4]*np.pi*aeff**2

plt.plot(wave, C_abs, label='n=1 without')
idx = np.where(C_abs == max(C_abs))
max_wave = np.round(wave[idx][0],3)


data = np.loadtxt('rod/Spectrum_n1.0_withshell')
data_sort = data[data[:,1].argsort(),]
aeff = data_sort[:,0]
wave = 1.240/data_sort[:,1]
C_ext = data_sort[:,2]*np.pi*aeff**2
C_abs = data_sort[:,3]*np.pi*aeff**2
C_sca = data_sort[:,4]*np.pi*aeff**2

idx = np.where(C_abs == max(C_abs))
max_wave = np.round(wave[idx][0],3)

plt.plot(wave, C_abs,label='n=1 with shell')



data = np.loadtxt('rod/Spectrum_withshell')
data_sort = data[data[:,1].argsort(),]
aeff = data_sort[:,0]
wave = 1.240/data_sort[:,1]
C_ext = data_sort[:,2]*np.pi*aeff**2
C_abs = data_sort[:,3]*np.pi*aeff**2
C_sca = data_sort[:,4]*np.pi*aeff**2

idx = np.where(C_abs == max(C_abs))
max_wave = np.round(wave[idx][0],3)

plt.plot(wave, C_abs,label='n=1.5 with shell')


data = np.loadtxt('rod/Spectrum_withoutshell')
data_sort = data[data[:,1].argsort(),]
aeff = data_sort[:,0]
wave = 1.240/data_sort[:,1]
C_ext = data_sort[:,2]*np.pi*aeff**2
C_abs = data_sort[:,3]*np.pi*aeff**2
C_sca = data_sort[:,4]*np.pi*aeff**2

idx = np.where(C_abs == max(C_abs))
max_wave = np.round(wave[idx][0],3)

plt.plot(wave, C_abs,label='n=1.5 without shell')


# data = np.loadtxt('rod/Spectrum_n1.0_withshell_likenoshell')
# data_sort = data[data[:,1].argsort(),]
# aeff = data_sort[:,0]
# wave = 1.240/data[:,1]
# C_ext = data_sort[:,2]*np.pi*aeff**2
# C_abs = data_sort[:,3]*np.pi*aeff**2
# C_sca = data_sort[:,4]*np.pi*aeff**2

# idx = np.where(C_abs == max(C_abs))
# max_wave = np.round(wave[idx][0],3)
# print('Gold', max_wave)

# plt.plot(wave, C_ext, 'tab:blue', linestyle=':')
# plt.plot(wave, C_abs, 'tab:orange', linestyle=':')
# plt.plot(wave, C_sca, 'tab:red', linestyle=':')






plt.xlabel('Energy [eV]')
plt.ylabel('Cross Section [$\mu$m$^2$]')
plt.legend(frameon=False)
plt.xlim([1, 2.5])
plt.show()

