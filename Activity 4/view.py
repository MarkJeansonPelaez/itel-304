from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def index():
    return render_template('index.html')

@views.route("/test")
def base():
    return render_template('base.html')

@views.route("/cv")
def cv():
    return render_template('cv.html')
@views.route('/website')
def website():
    return render_template('index2.html')
@app.route('/resume')
def resume():
    return render_template('index3.html')
