import numpy as np
import matplotlib.pyplot as plt
plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)
font = {'family': 'serif',

        'weight': 'normal',
        'size': 16,
        }
y1 = np.loadtxt('1ControlResut.txt',delimiter=',')
y2 = np.loadtxt('Def_Inp.txt')
fig = plt.figure(figsize=(8,6))  #setting the figure size
plt.plot(y1[:,1],color='r',marker='o', label='ANN',lw=2) # plotting the scatter plot
plt.plot(y2,color='b',marker='*',label='Target Path',lw=2) # plotting the scatter plot
plt.xlabel('Steps',fontdict=font)
plt.ylabel('Deflection (m)',fontdict=font)
plt.xlim([1,45])
plt.legend(fontsize="18")
plt.show()



