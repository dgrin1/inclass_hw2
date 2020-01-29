i=0
s=0
#initialize variables

N_string=input("What is Nmax?")
N=int(N_string)
#read in Nmax

#print(N)

#iterate while i<Nmax
while i<N:
	i=i+1
#increment i
	s+=1/i	
#increment harmonic sum

#print sum
print(s)