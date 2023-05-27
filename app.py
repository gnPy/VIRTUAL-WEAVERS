from module import predict, get_details, get_row_as_dict
from flask import Flask, render_template
import sys
import pandas as pd
sys.path.append('templates')


app = Flask(__name__)

l = predict(31415)
get_details(predict(31415))

df=pd.read_csv("Datasets/temp.csv")
temp=df[['title','coverImg','rating','language']]
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

@app.route('/dashboard')
def dash():
    return render_template('dash.html', dictionary=dictionary, number=len(dictionary['title']))

@app.route('/book/<title>')
def book(title):
    print(title)
    row_dict=get_row_as_dict(df,title)
    return render_template('book.html',title=title, dictionary=row_dict)


if __name__ == '__main__':
    app.run(debug=True)
