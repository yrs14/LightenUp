from flask import Flask
app = Flask(__name__)

@app.route('/insert_data/<int:height>')
def getdata(height):
    return 'your heigt is'+height+'m'
	
if __name__ == '__main__':
    app.run()