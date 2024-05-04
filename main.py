#from flask import Flask
#from flask_cors import CORS

#app = Flask(__name__)
#CORS(app)
    
#@app.route('/', methods=["POST"])
#def hola_mundo():
#    return 'Hola Mundo!!'

#if __name__ == '__main__':
#    app.run(debug=True)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_t
