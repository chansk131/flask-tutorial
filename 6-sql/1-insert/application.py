import os

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'database.db'))
engine = create_engine('sqlite:///' + path)
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)


@app.route("/flights/create", methods=["GET", "POST"])
def create_flight():
    # Create a flight

    if request.method == 'POST':
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        duration = request.form.get("duration")

        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)", {
            "origin": origin, "destination": destination, "duration": duration})
        db.commit()
        return redirect(url_for("index"))

    return render_template("create_flight.html")
