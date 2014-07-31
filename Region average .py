import csv

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
