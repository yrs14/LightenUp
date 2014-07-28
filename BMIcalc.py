def calcBMI(height,weight,measure):
	BMI = 0
	BMI += weight
	BMI = BMI/(height^2)
	if measure == "imperial":
		BMI = BMI * 703
	return(BMI)

