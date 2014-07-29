import csv

def csvToArray(strPath):
    with open (strPath,"r") as csvfile:
        arrImport = csv.reader(csvfile, delimiter=',', quotechar='|')
        arrRead = []
        for arrWrite in arrImport:
            arrRead.append(arrWrite)
    return arrRead

def sortTables(strPath):
    arrData = csvToArray(strPath)

    ## Inside each array, the data is ordered Men = 1, Women = 0.

    ## Data relating to BMI
    arrBMI = []
    arrBMI.append({"Blood pressure":arrData[13:18],"Longstanding Illness":arrData[96:98],"GHQ12":arrData[165:168]})
    arrBMI.append({"Blood pressure":arrData[6:11],"Longstanding Illness":arrData[91:94],"GHQ12":arrData[160:163]})

    ## Data goes from overall - underweight (less than 18.5) - normal (18.5 - 25) - overweight (25-30) - obese/morbidly obese (over 30)

    ## Data relating to Waist Circumference
    arrWaist = []
    arrWaist.append({"Blood pressure":arrData[56:61],"Longstanding Illness":arrData[131:134]})
    arrWaist.append({"Blood pressure":arrData[49:54],"Longstanding Illness":arrData[126:129]})

    ## Data goes from overall - raised (above 102cm in men and 88cm in women) - unraised (below 102cm/88cm)
    

    del arrData

    for int1 in range(len(arrBMI)):
        for strKey in arrBMI[int1]:
            dicTemp = {}
            for int2 in range(len(arrBMI[int1][strKey])):
                dicTemp[arrBMI[int1][strKey][int2][0]] = arrBMI[int1][strKey][int2][1:]
            for strKeyTemp in dicTemp:
                for intTemp in range(len(dicTemp[strKeyTemp])):
                    try:
                        dicTemp[strKeyTemp][intTemp] = int(dicTemp[strKeyTemp][intTemp])
                    except:
                        try:
                            dicTemp[strKeyTemp][intTemp] = int(dicTemp[strKeyTemp][intTemp][1:-1])
                        except:
                            try:
                                dicTemp[strKeyTemp][intTemp] = int(dicTemp[strKeyTemp][intTemp][1:])
                            except:
                                dicTemp[strKeyTemp][intTemp] = int(dicTemp[strKeyTemp][intTemp][:-1])

            arrBMI[int1][strKey] = dicTemp

    for int1 in range(len(arrWaist)):
        for strKey in arrWaist[int1]:
            dicTemp = {}
            for int2 in range(len(arrWaist[int1][strKey])):
                dicTemp[arrWaist[int1][strKey][int2][0]] = arrWaist[int1][strKey][int2][1:]
            for strKeyTemp in dicTemp:
                for intTemp in range(len(dicTemp[strKeyTemp])):
                    try:
                        dicTemp[strKeyTemp][intTemp] = int(dicTemp[strKeyTemp][intTemp])
                    except:
                        try:
                            dicTemp[strKeyTemp][intTemp] = int(dicTemp[strKeyTemp][intTemp][1:-1])
                        except:
                            try:
                                dicTemp[strKeyTemp][intTemp] = int(dicTemp[strKeyTemp][intTemp][1:])
                            except:
                                dicTemp[strKeyTemp][intTemp] = int(dicTemp[strKeyTemp][intTemp][:-1])

            arrWaist[int1][strKey] = dicTemp

    return arrBMI, arrWaist
