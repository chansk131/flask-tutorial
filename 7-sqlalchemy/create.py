import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
database_url = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database.sqlite'))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
