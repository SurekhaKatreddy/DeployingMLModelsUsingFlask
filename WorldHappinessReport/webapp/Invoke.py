import os
import numpy as np
import pandas as pd
import flask
import pickle
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

def ValuePredictor(to_predict_list):
    #to_predict = np.array(to_predict_list).reshape(1,10)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict_list)
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        print(to_predict_list)
        
        #build dummy data
        inference_df = pd.DataFrame(to_predict_list, index=[0])
        
        
        #inference_df.reset_index()
        test_df = pd.DataFrame({'Country': ['Sweden','Slovakia'],
                           'Region': ['Western Europe','Central and Eastern Europe'],
                           'Standard Error': [0.03157,0.04267],
                            'Economy (GDP per Capita)': [1.33171, 1.16891],      
                            'Family':[1.33171, 1.16891],
                            'Health (Life Expectancy)': [1.28907,1.26999],
                            'Freedom': [0.91087,0.78902],
                            'Trust (Government Corruption)':[0.43844,0.03431],
                            'Generosity':[0.36262,0.36262],
                            'Dystopia Residual': [2.37119,2.24639]})
        
        #test = ['Sweden', 'Western Europe', 0.03157, 1.33171, 1.33171, 1.28907, 0.91087, 0.43844, 0.36262, 2.37119]
        result = ValuePredictor(inference_df)
        return render_template("result.html",
                               country = inference_df['Country'][0], 
                               region = inference_df['Region'][0], 
                               std_err = inference_df['Standard Error'][0],
                               economy = inference_df['Economy (GDP per Capita)'][0],
                               family = inference_df['Family'][0],
                               health = inference_df['Health (Life Expectancy)'][0],
                               freedom = inference_df['Freedom'][0],
                               trust = inference_df['Trust (Government Corruption)'][0],
                               generosity = inference_df['Generosity'][0],
                               dystopia = inference_df['Dystopia Residual'][0],
                               prediction=result)
