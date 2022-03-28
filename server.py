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
  images = ["https://upload.wikimedia.org/wikipedia/lv/thumb/b/b5/Olga_Rajecka.JPG/1200px-Olga_Rajecka.JPG","https://upload.wikimedia.org/wikipedia/lv/thumb/b/b5/Olga_Rajecka.JPG/1200px-Olga_Rajecka.JPG","https://upload.wikimedia.org/wikipedia/lv/thumb/b/b5/Olga_Rajecka.JPG/1200px-Olga_Rajecka.JPG"]
  return render_template("test.html", parametri=parametri,images=images)

@app.route('/about')
def about():
    return render_template("about.html")    
    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run(debug="true")
