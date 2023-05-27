from module import predict, get_details
from flask import Flask, render_template , url_for
import sys
import pandas as pd
sys.path.append('templates')


app = Flask(__name__)

l = predict(31415)
get_details(predict(31415))

temp=pd.read_csv("Datasets/temp.csv")
dictionary=dict()
for column in temp:
    dictionary[column] = list(temp[column])

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/recommend')
def recom():
    return render_template('recommendation.html', dictionary=dictionary, number=len(dictionary['title']))

if __name__ == '__main__':
    app.run(debug=True)
