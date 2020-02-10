from __future__ import division,print_function
import matplotlib.pyplot as plt
import numpy as np

#go into interactive mode
plt.ion()

#Use Latex fonts
plt.rc('text',usetex=True)
plt.rc('font',**{'family':'serif','serif':['Palatino']})
#dense x grid for theory curve
x=np.logspace(1.e-5,2*3.14159,1000)

#y values for sin good theory
y=np.abs(np.sin(x)*np.exp(-x))

#y values list for bad sin theory
ybad=np.abs(np.cos(x)*np.exp(-x))

##two panel subplots
plt.subplot(211)
#plt.yscale('log')


#coarsely gridded "data"
xdata=np.logspace(1.e-5,2*3.14159,100)

#make data points obey sin curve
ydata=np.abs(np.sin(xdata))*np.exp(-xdata)

#Add label
a=plt.plot(x,y,label='theory')
plt.setp(a,linewidth=4)

#plot "data"
plt.plot(xdata,ydata,'b*',color='#FF0000',label='data',markersize=14)

#Plot title
plt.title('Climate change is scary')

#axis labels
plt.xlabel('Time')
plt.ylabel('Height of ocean in meters')

#limits
#plt.xlim([0,6])
#plt.ylim([.001,10])

#put down a legend
plt.legend(loc=1)

#move to next panel
plt.subplot(212)
#axis labels
plt.xlabel(r'$\omega t$',fontsize=24)
plt.ylabel('Height of ocean in meters')

#limits again
plt.xlim([0,6])
plt.ylim([.001,100])

#plot bad cosine fit
plt.plot(x,y,'r',label='bad theory')
plt.yscale('log')
plt.legend(loc=1)
#plot additional data points
plt.plot(xdata,ydata,'r^',label='data',markersize=14)
plt.errorbar(xdata,ydata,xerr=.05,yerr=.007,fmt='r^',capsize=5,markersize=14,label='data')

plt.grid()
# 
# 
# 
# 
plt.show()
# plt.savefig('test.pdf',format='pdf')

