# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:13:52 2021

@author: Shashi
"""

from flask import Flask , render_template,request
import pickle
import joblib
model = pickle.load(open("profit.pkl","rb"))
ct = joblib.load("column")
app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/display' ,methods = ['POST'])
def display():
    ms = request.form['ms']
    ad = request.form['as']
    rd = request.form['rs']
    state = request.form['s']
    data = [[ms,ad,rd,state]]
    pred = model.predict(ct.transform(data))
    print(pred)
    return render_template("index.html",y = str(pred[0]))
    
@app.route('/admin')
def admin():
   return "Admin Flask"
   
@app.route('/user/<name>')
def user(name):
   return "Hello "+name+" welcome to the webpage"


if __name__=='__main__':
    app.run(debug = True)