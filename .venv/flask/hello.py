from flask import Flask
# Flask application instance 
## __name__ holds the current Python module
app = Flask(__name__) 

# app.route as a decorator
## will respond to web request for URL /, the main URL
@app.route('/')
# function that returns an HTTP response 
## turn a func in python to Flask view
def home():
    return 'Hello, Flask'