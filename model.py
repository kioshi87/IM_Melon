from flask import Flask
import flask_sqlalchemy 
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Melon(db.Model):
    """Melons table."""

    __tablename__ = "melons"

    melon_name = db.Column(db.String(50), 
                       primary_key=True,
                       
                       )
    melon_qty = db.Column(db.Integer, nullable=False)
    melon_type = db.Column(db.String(50))
    melon_season = db.Column(db.String(50))

    def __repr__(self):
        return f'<Melon melon_name={self.melon_name}>'

    

class Subscriber(db.Model):
    """Subscribers table."""

    __tablename__ = "subscribers"

    subscriber_number = db.Column(db.String(15), 
                       primary_key=True)
    #melon_name = db.Column(db.String,
                       #db.ForeignKey("melons.melon_name")
                       #)
    
    name = db.Column(db.String(200))
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'<Subscriber subscriber_number={self.subscriber_number} name={self.name} email={self.email} password={self.password}>'


def connect_to_db(flask_app, db_uri='postgresql:///melon', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app
    
    connect_to_db(app)
