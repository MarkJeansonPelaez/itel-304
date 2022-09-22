from flask import  Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <h2>Hello and Welcome </h2>
            <form action="/greet">
                What's your name? <input type='text' name='username'><br>
                What is your favorite food? <input type='text' name='favfood'><br>
                What's your characteristics? <input type='text' name='characteristics'><br>
                What's your age? <input type='text' name='age'><br>
                <input type='submit' value='Continue'>
            </form>
        </body></html>
        """
@app.route('/greet')
def greet():
    name = request.args.get('username', 'World')
    characteristics = request.args['characteristics']
    favfood = request.args['favfood']
    age = request.args['age']
    if characteristics == '':
        msg = 'You did not tell me your characteristics.'
    else:
        msg = name +' is '+ characteristics +' favorite food is '+ favfood +' age is ' + age

    return """
        <html><body>
            <h2>Hello, {0}!</h2>
            {1}
        </body></html>
        """.format(name,msg)

#Launch the FlashPy dev server
app.run(host="localhost", debug=True)
