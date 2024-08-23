from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello__world():
    return "Hello, Simple Flask application"
