from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hola_mundo():
    return 'Hola Mundo'

@app.route('/shao')
def shao_mundo():
    return 'Shao Mundo'

if __name__ == '__main__':
    app.run(debug=True)
