from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Default Index Route"

@app.route("/second")
def second():
    return "Second Route"