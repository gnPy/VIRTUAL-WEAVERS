from module import predict, get_details, get_row_as_dict, f
from flask import Flask, render_template
import sys
import pandas as pd
import numpy as np


sys.path.append('templates')


app = Flask(__name__)

l = predict(31415)
get_details(predict(31415))

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

'''
test=pd.read_csv("Datasets/general_books.csv")
test=test[['rating','title']]
test['rating'] = test['rating'].replace(np.nan, 0)
test['rating'] = test['rating'].apply(f)
all_titles=test['title'].head(10)
print(list(all_titles))
'''
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
    return render_template('dash.html', dictionary=dictionary, number=len(dictionary['title']), titles=top_titles)

@app.route('/book/<title>')
def book(title):
    df=pd.read_csv("Datasets/details.csv")
    print(title)
    row_dict=get_row_as_dict(df,title)
    return render_template('book.html',title=title, dictionary=row_dict)


if __name__ == '__main__':
    app.run(debug=True)
