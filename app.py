from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/tony')
def testfunction():
    return "Tony"



app.run()