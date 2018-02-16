for x in range(0,100000):
	x_s = str(x)
	y = x_s[::-1]
	y = int(y)
	z = x * y
	z_s = str(z)
	
	if z_s== z_s[::-1]:
		print(x,y,z_s)