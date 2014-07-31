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
	for regionnumber in range (0,len(array)):
		if userregion == array[regionnumber][0]:
			usernumber = regionnumber
	sortarray = array[usernumber][1:]
	for intTemp in range(len(sortarray)):
		sortarray[intTemp] = float(sortarray[intTemp])
	if userBMI >= sortarray[99]:
		print ("you are in the 100th percentile")
	elif userBMI <= sortarray[1]:
		print ("you are in the 1st percentile")	
	else:
		print("you are in the ",str(spiltsort(userBMI,sortarray)) + "th percentile of this area")

def spiltsort(BMI,array):
	maxbound = 99
	minbound = 0
	while maxbound != minbound:
		intTest = int((maxbound+minbound)/2)
		if array[intTest] == BMI:
			return intTest
		elif array[intTest] > BMI:
			maxbound = intTest
		elif array[intTest] < BMI:
			minbound = intTest

#if 
# when runing this code add to the final line in your magical way
# userinput(their BMI input,what region they say they come from,csvToArray("/home/kay/Desktop/percentileestimates.csv")

#print(userinput,28,"Shropshire",csvToArray("/home/kay/Desktop/percentileestimates.csv"))

