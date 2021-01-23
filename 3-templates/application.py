from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<string:name>")
def index(name):
    return render_template("index.html", username=name)

@app.route("/greater-than-ten")
def greater_than_ten():
    return render_template("greater_than_ten.html", value=11)

@app.route("/notes")
def notes():
    notes = [
        "First note",
        "Second note"
    ]
    return render_template("note.html", notes=notes)