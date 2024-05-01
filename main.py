from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app = Flask(__name__)
@app.route('/shao')
def shao_mundo():
    return 'Shao Mundo'
    
@app.route('/hola')
def hola_mundo():
    return 'Hola Mundo'

if __name__ == '__main__':
    app.run(debug=True)
