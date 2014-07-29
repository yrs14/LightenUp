from flask import Flask
app = Flask(__name__)

@app.route('/insert_data/<int:height>')
def getdata(height):
    return 'your heigt is'+height+'m'

@app.route('/')
def index():
    f =open("questions.html","r+")
    return f.read()


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1')
