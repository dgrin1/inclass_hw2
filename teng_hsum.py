#!/usr/bin/env python

# read in max index value
N=int(input("N="))

# starting indices
n=1
hsum=0

# iterate the sum
while n<=N:
    hsum+=(1/n)
    n+=1

# print sum    
print(hsum)
