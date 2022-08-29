# this is python module

from crypt import methods
import numpy as np 
import pandas as pd


from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Default API"


@app.route('predict', methods = ['GET','POST'])
def predict():
    # prediction logic 
    return "API"

if __name__ == "__main__":
    app.run(debug=True)
