import csv

def search(search,averagedic):
	for region in array:
		if search.upper() == region.upper():
			return averagedic[region]

def csvToArray(strPath):
    with open (strPath,"r") as csvfile:
        arrImport = csv.reader(csvfile, delimiter=',', quotechar='|')
        arrRead = []
        for arrWrite in arrImport:
            arrRead.append(arrWrite)
    return arrRead	

def regionaverage(array)
	averagedic = {}
	for region in array:
		averagedic[region[1]] = region[50]
	return averagedic

averagedic = regionaverage(csvToArray('adress of CSV'))
#to find out the average of the region do search(userinput,averagedic)

