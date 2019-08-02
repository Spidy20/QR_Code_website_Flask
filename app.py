from qr import qrgen
from flask import  Flask,render_template
from flask import *

app = Flask(__name__)


@app.route('/QR_Code_Generater')
def home():
    return render_template('index.html')

@app.route('/converted',methods = ['POST'])
def convert():
    global tex
    tex = request.form['test']
    return render_template('converted.html')

@app.route('/download')
def download():
    qrgen(tex)
    filename = tex+'.png'
    return send_file(filename,as_attachment=True)

if __name__ == "__main__":
     app.run(debug=True)