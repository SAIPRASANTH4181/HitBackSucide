from flask import Flask, send_file
from flask_cors import CORS, cross_origin
from flask import request
import os

import pandas as pd
import itertools
# from werkzeug import secure_filename

UPLOAD_FOLDER = 'C:/Users/bsaip/OneDrive/Desktop/PSD-Project/HitBackSucide'
app = Flask(__name__)
app.config["CLIENT_CSV"]= UPLOAD_FOLDER

CORS(app)
@app.route('/get_image')
def get_image():
    filename = 'N2.png'
    return send_file(filename, mimetype='image/jpg')

@app.route("/",methods = ['GET' , 'POST'])
def helloWorld():
     if request.method == 'POST':
        f = request.files['file']
        # filename = secure_filename(f.filename)
        f.save(os.path.join(app.config["CLIENT_CSV"], f.filename))
        import aspect_analysis
        return 's2'
     if request.method == 'GET':
        
        return 'File-Uploaded'
   

@app.route('/update' , methods = ['GET' , 'POST'])
class FileUploader():
 def upload_file():
       if request.method == 'POST':
        f = request.files['file']
        # filename = secure_filename(f.filename)
        f.save(os.path.join(app.config["CLIENT_CSV"], f.filename))
        return 'File Uploaded'
print('dddddddddddddddd')    
app.run(debug=True)



# app = Flask(__name__)
# 
