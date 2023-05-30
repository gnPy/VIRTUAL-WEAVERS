from flask import render_template, flash, redirect, url_for
import pandas as pd

from app.module import predict, get_details, get_row_as_dict
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('dashboard'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/dashboard')
def dashboard():
    dictionary=get_details(predict(user['userID']))
    return render_template('dash.html', dictionary=dictionary, number=len(dictionary['title']), titles=top_titles, title='Dashboard')

@app.route('/book/<title>')
def book(title):
    df=pd.read_csv("Datasets/details.csv")
    row_dict=get_row_as_dict(df,title)
    return render_template('book.html',title=title, dictionary=row_dict)


if __name__ == '__main__':
    app.run(debug=True)
