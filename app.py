from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test')
def text():
    return render_template('base.html')
@app.route('/cv')
def cv():
    return render_template('cv.html')
@app.route('/website')
def website():
    return render_template('index2.html')
@app.route('/resume')
def resume():
    return render_template('index3.html')


app.run(host="localhost", debug=True)
