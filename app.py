# coding:utf-8
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html',message='hello!')
@app.route('/youzumi')
def youzumi():
    return render_template('index.html',message='用済みだ、消えろニャ')

if __name__ == "__main__":
    app.run(host='0.0.0.0')