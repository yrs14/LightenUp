from flask import Flask,request,render_template,url_for

app = Flask(__name__)

#Males only require total body weight and waist measurement

#Females require:
#total body weight
#wrist measurement at fullest point,
#hip measurement at naval
#forearm measurement at fullest point

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

def calcBMI(height,weight):
    BMI = 0
    BMI = weight/(height^2)
    #if measure == "imperial":
    #    BMI = BMI * 703
    return(BMI)

#@app.route('/')
#def index():
#    f=open("questions.html","r+")
#    return f.read()
#use below for a template

@app.route('/')
def resultstemplate():
    return render_template('questions.html', head='Fat Check')

@app.route('/', methods=['POST'])
def measurements():
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    #measure = request.form['measure']
    age = int(request.form['age'])
    gender = request.form['gender']
    waist = request.form['waist']
    wrist = request.form['wrist']
    hip = request.form['hip']
    forearm = request.form['forearm']
    totalbody = request.form['totalbody']
    bmi=str(calcBMI(height,weight))
    if gender == "m" or "M":
            malefatcalc(waist,totalbody)
    elif gender == "f" or "F":
            femfatcalc(wrist,waist,hip,forearm,totalbody)
    #return these onto results.html

if __name__ == '__main__':
    app.run(host='0.0.0.0')
