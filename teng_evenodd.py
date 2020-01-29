#!/usr/bin/env/python

#read in number
number=float(input("give me a number "))
print(number)
#calculate remainder
remainder=number%2

#report back
if remainder==0:
    print(number," is even")
elif remainder==1:
    print(number," is odd")
else:
	print("not an integer")