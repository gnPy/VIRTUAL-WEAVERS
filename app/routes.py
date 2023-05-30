from flask import render_template, flash, redirect, url_for, request
import pandas as pd
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app.module import predict, get_details, get_row_as_dict
from app import app
from app.forms import LoginForm
from app.models import User

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
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard():
    dictionary=get_details(predict(current_user.id))
    return render_template('dash.html', dictionary=dictionary, number=len(dictionary['title']), titles=top_titles, title='Dashboard')

@app.route('/book/<title>')
def book(title):
    df=pd.read_csv("Datasets/details.csv")
    row_dict=get_row_as_dict(df,title)
    return render_template('book.html',title=title, dictionary=row_dict)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))