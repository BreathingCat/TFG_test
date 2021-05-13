from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "I am a lightweight flask web application"