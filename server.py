from flask import Flask,request,render_template,url_for

app = Flask(__name__)

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
    bmi=str(weight/height^2)
    return bmi

if __name__ == '__main__':
    app.debug = True
    app.run()
