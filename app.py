from flask import Flask, render_template, session, redirect, url_for, session
import numpy as np
import pickle
import pandas as pd  

app = Flask(__name__)


# REMEMBER TO LOAD THE MODEL AND THE SCALER!



@app.route('/', methods=['GET', 'POST'])
def index():
    # # Create instance of the form.
    return render_template('home.html')


@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)