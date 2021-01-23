import os

from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)
database_url = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database.sqlite'))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)


@app.route("/flights/create", methods=["GET", "POST"])
def create_flight():
    # Create a flight

    if request.method == 'POST':
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        duration = request.form.get("duration")

        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("create_flight.html")