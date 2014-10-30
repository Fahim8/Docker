from flask import Flask
from flask import request
app = Flask(__name__)

import os, sys

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/1")
def hello():
    return "Hello people!"




@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)





@app.rouste ("/listfile")
def files():
    path = "./uploads"
    x = os.listx (path)
    
    for file in x:
    files = str (files +file + " ")

    return files

