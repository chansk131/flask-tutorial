import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

database_url = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database.db'))
engine = create_engine('sqlite:///' + database_url)
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)