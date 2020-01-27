from __future__ import division,print_function

from numpy import loadtxt,array,dot
s=0
t=0.1
k=0
while k <100:
	k+=1
	s+=1./k
#	t*=1./k
print(s)
