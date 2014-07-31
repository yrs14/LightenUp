def BMIcategory(BMI):
	if BMI <= 18:
		return("Underweight")
	elif BMI <= 24:
		return("Healthy")
	elif BMI <= 29:
		return("Overweight")
	elif BMI <= 39:
		return("Obese")
	else:
		return("Fat bastard")#actually Extremly Obese

usercategories = BMIcatigory(userinputBMI)
