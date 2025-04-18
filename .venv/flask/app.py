from flask import Flask, render_template
# Flask application instance 
## __name__ holds the current Python module
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')