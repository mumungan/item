from flask import Flask, render_template
import pandas as pd
from forex_python.converter import CurrencyRates
from datetime import datetime, date
import requests
import json
 
app = Flask(__name__)
 
@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/layout')
def layout():
   return render_template('layout.html')   

@app.route('/citruswork')
def citruswork():
   return render_template('citruswork.html')   

@app.route('/pesticide')
def pesticide():
   return render_template('pesticide.html')   

@app.route('/cymbidiumdisease')
def cymbidiumdisease():
   return render_template('cymbidiumdisease.html')      

if __name__ == '__main__':
   app.run(debug=True)