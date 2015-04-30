# partial-3
#Valdez, Patricia
#Estimating e


def calculuate_e(x):
	y = x
	e=(1+1/y)**y
	return float(e)


	
pre = int(input("Dame el numero de decimales: "))

z = calculuate_e(pre)

print("the number is: ",z)
