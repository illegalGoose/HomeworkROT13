from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! gre,glrg'

@app.route('/about')
def about():
    return 'About'