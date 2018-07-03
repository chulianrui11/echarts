from flask import Flask, render_template
app = Flask(__name__)


@app.route("/pie")
def pie():
    return render_template('pie.html')


@app.route("/bar")
def bar():
    return render_template('bar.html')


@app.route("/bar_mul")
def bar_mul():
    return render_template('bar_multi.html')
