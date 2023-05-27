from module import predict
from flask import Flask, render_template , url_for
import sys
import pandas as pd
sys.path.append('templates')


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    result = predict(31415)
    data = {'result': result}
    return render_template('index.html', data=data)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/recommend')
def recom():
    return render_template('recommendation.html')

if __name__ == '__main__':
    app.run(debug=True)
