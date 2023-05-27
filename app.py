from module import predict
from flask import Flask, render_template
import sys
import pandas as pd
sys.path.append('templates')


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    result = predict(1)
    data = {'result': result}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)