#Valdez Patricia
#A01233330

filedata = open("93cars.dat.txt")
cmpg=0
hmpg=0
costo=0
lineas=0 #Contador de lineas leidas
coches=0
for line in filedata: 
	if (lineas%2==0):
		cmpg=cmpg+float(line[52:54])
		hmpg=hmpg+float(line[55:57])
		costo=costo+float(line[42:46])
		coches=coches+1
		
	lineas=lineas+1
coches=lineas/2
ca=round(cmpg/coches,7) #promedio en la ciudad
ha=round(hmpg/coches,7) #promedio en la carreteta
costoa=round(costo/coches,7) #promedio costo

print("Existen ",coches," diferentes")
print("El promedio de gasolina en la ciudad es de: ",ca)
print("El promedio de gasolina en la carretera es de: ",ha)
print("El promedio del costo de los coches es de: ",costoa)

print()
