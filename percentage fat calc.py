#Males only require total body weight and waist measurement

#Females require:
#total body weight
#wrist measurement at fullest point,
#hip measurement at naval
#forearm measurement at fullest point

If gender == "m": or "M":
	malefatcalc(waist,totalbody)
Elif gender == "f" or "F":
	femfatcalc(wrist,waist,hip,forearm,totalbody)

def malefatcalc(waist,totalbody):	
	factor1 = (totalbody * 1.082) +94.42
	factor2 = waist * 4.15
	leanbody = factor1 - factor2		
	fat = totalbody - leanbody
	fatper = fat*100/totalbody
	return(fatper)

def femfatcalc(wrist,waist,hip,forearm,totalbody):
	factor1 = (totalbody * 0.732) + 8.987
	factor2 = wrist / 3.140
	factor3 = waist * 0.157 	
	factor4 = hip * 0.157
	factor5 = forearm * 0.434
	leanbody = factor1 + factor2 - factor3 - factor4 + factor5
	fat = totalbody - leanbody 
	fatper = fat * 100 / totalbody
	return(fatper)

# Sauce = http://www.bmi-calculator.net/body-fat-calculator/body-fat-formula.php
