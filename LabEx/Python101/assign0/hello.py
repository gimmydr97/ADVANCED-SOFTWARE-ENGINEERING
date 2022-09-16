from flask import Flask
app = Flask(__name__)
@app.route('/')
def root():
return "Welcome! I'm flask!"
@app.route('/<name>')
def greet(name):
return "Hello, {}! It's great to meet you.".format(name)