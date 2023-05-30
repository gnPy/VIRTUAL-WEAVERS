from module import predict, get_details, get_row_as_dict
from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

user={'username':'Pradyumn', 'userID':31415}


top_titles=['The Hunger Games', 
            'Harry Potter and the Order of the Phoenix', 
            'To Kill a Mockingbird', 
            'Pride and Prejudice', 
            'Twilight', 
            'The Book Thief', 
            'Animal Farm', 
            'The Chronicles of Narnia', 
            'J.R.R. Tolkien 4-Book Boxed Set: The Hobbit and The Lord of the Rings', 
            'Gone with the Wind']


@app.route('/index')
def home():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template("login.html", title="Login")

@app.route('/')
@app.route('/dashboard')
def dash():
    dictionary=get_details(predict(user['userID']))
    return render_template('dash.html', dictionary=dictionary, number=len(dictionary['title']), titles=top_titles, title='Dashboard')

@app.route('/book/<title>')
def book(title):
    df=pd.read_csv("Datasets/details.csv")
    row_dict=get_row_as_dict(df,title)
    return render_template('book.html',title=title, dictionary=row_dict)


if __name__ == '__main__':
    app.run(debug=True)
