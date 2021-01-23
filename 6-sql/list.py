import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

database_url = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database.db'))
engine = create_engine('sqlite:///' + database_url)
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT * FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minute")

if __name__ == "__main__":
    main()