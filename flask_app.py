# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 12:40:20 2021

@author: Poojan
"""

import numpy as np 
import pickle 
import pandas as pd 
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

#Use model from pickle file
pred_model = pickle.load(open('fish_classification.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods =['POST'])
def prediction():
    
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = pred_model.predict(final_features)
    species = {0: 'Bream', 1: 'Parkki', 2: 'Perch', 3: 'Pike', 4: 'Roach', 5: 'Smelt', 6: 'Whitefish'}

    return render_template('index.html', prediction_text='The fish belongs to species {}'.format(species.get(prediction[0])))

if __name__ == '__main__':
    app.run()