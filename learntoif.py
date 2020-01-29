whole=int(input("Choose an integer less than 7"))
#read in a number

if whole > 7:
	print(whole, "is larger than 7. You chose badly. I will fix taht for you.")
	whole=5
	print(whole,"is smaller than 7. Better choice. Ha ha!")
elif whole>5:
	print("You're ok but cutting it awfully close.")
else:
	print("Great job.")