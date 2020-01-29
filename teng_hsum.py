#!/usr/bin/env python

# read in max index value
N=int(input("N="))
n=1
hsum=0
while n<=N:
    hsum+=(1/n)
    n+=1
print(hsum)
