import csv

def csvToArray(strPath):
    with open (strPath,"r") as csvfile:
        arrImport = csv.reader(csvfile, delimiter=',', quotechar='|')
        arrRead = []
        for arrWrite in arrImport:
            arrRead.append(arrWrite)
    return arrRead	

def userinput(userBMI,userregion,array):
	regionnumber = 0
	usernumber = 0
	for regionarray in array:
		regionnumber +=1
		if userregion == regionarray[1]:
			usernumber = regionnumber
	sortarray = array [1:]
	if userBMI >= sortarray[100]:
		print ("you are in the 100th percentile")
	elif userBMI <= sortarray[1]:
		print ("you are in the 0th percentile")	
	else:
		print("you are in the ",str(spiltsort(userBMI,0,100,sortarray)) + "th percentile of this area")

def spiltsort(BMI,minbound,maxbound,array):
	if maxbound - minbound > 2:
#	if maxbound -minbound != 1 (unsure which one to use)
		guess = round(((minbound + maxbound)/2),2)
		if BMI > array[guess]:
			spiltsort(BMI,(guess-1),maxbound,array)
		else:
			spiltsort(BMI,minbound,guess,array)
	else:
		return (maxbound)

#if 
# when runing this code add to the final line in your magical way
# userinput(their BMI input,what region they say they come from,csvToArray("/home/kay/Desktop/percentileestimates.csv")

#print(userinput,28,"Shropshire",csvToArray("/home/kay/Desktop/percentileestimates.csv"))

