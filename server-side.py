from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

def calcBMI(height,weight):
    BMI = 0
    BMI = weight/(height^2)
    #if measure == "imperial":
    #    BMI = BMI * 703
    return(BMI)

@app.route('/')
def index():
    f=open("questions.html","r+")
    return f.read()
#use below for a template
#@app.route('/resultspage.html')
def resultstemplate():
    return render_template('resultspage.html', name=None)

@app.route('/', methods=['POST'])
def my_form_post():
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    #measure = request.form['measure']
    age = int(request.form['age'])
    gender = request.form['gender']
    bmi=str(weight/height^2)
    return bmi

if __name__ == '__main__':
    app.debug = True
    app.run()
