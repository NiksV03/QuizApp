from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def index():
  return render_template("index.html")

@app.route('/test',methods = ['POST', 'GET'])
def test():
  parametri = ["IQ","Augums","Kājas izmērs"]
  return render_template("test.html", parametri=parametri)

@app.route('/about')
def about():
    return render_template("about.html")    
    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run(debug="true")
