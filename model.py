from flask import Flask
import flask_sqlalchemy 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# app = Flask(__app__)
# db_uri = "postgresql:///melon"

db = SQLAlchemy()



class AlertSystem(db.Model):
    """Alert System table."""

    __tablename__ = "alertsystem"

    id = db.Column(db.Integer,  
                       primary_key=True,
                       autoincrement=True,
                       )
    # not sure if alertsystem table needs an ID column
    # if not, table does not have a primary key
    melon_name = db.Column(db.String, 
                        db.ForeignKey("melons.melon_name")
                        )
    subscriber_number = db.Column(db.Integer, 
                        db.ForeignKey("subscribers.subscriber_number")
                        )
    message_id = db.Column(db.Integer, 
                        db.ForeignKey("messages.message_id")
                        )   
    melons = db.relationship("AlertSystem", backref = "melons")
    messages= db.relationship("AlertSystem", backref = "messages")
    subscribers = db.relationship("AlertSystem", backref = "subscribers")

    def __repr__(self):
        return f'<AlertSystem id={self.id} melon_name={self.melon_name} subscriber_number={self.subscriber_number} message_id={self.message_id}>'


class Melons(db.Model):
    """Melons table."""

    __tablename__ = "melons"

    melon_name = db.Column(db.String(50), 
                       primary_key=True,
                       
                       )

    subscriber_number = db.Column(db.Integer, 
                        db.ForeignKey("subscribers.subscriber_number"),
                        )
    melon_qty = db.Column(db.Integer, nullable=False)
    melon_type = db.Column(db.String(50), nullable=False)
    melon_season = db.Column(db.String(50), nullable=True)


class Messages(db.Model):
    """Messages table."""

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, 
                       primary_key=True,
                       autoincrement=True,
                       )

    subscriber_number = db.Column(db.Integer, 
                        db.ForeignKey("subscribers.subscriber_number"),
                        )
    melon_name = db.Column(db.String(50), 
                        db.ForeignKey("melons.melon_name"),
                        )
    season_alert = db.Column(db.String(50), nullable=False)
    qty_alert = db.Column(db.String(50), nullable=False)
    type_alert = db.Column(db.String, nullable=True)   

    

    def __repr__(self):
        return f'<Messages message_id={self.message_id}>'

    

class Subscribers(db.Model):
    """Subscribers table."""

    __tablename__ = "subscribers"

    subscriber_number = db.Column(db.Integer, 
                       primary_key=True,
                       autoincrement=True,
                       )
    melon_name = db.Column(db.String,
                       db.ForeignKey("melons.melon_name")
                       )
    
    subscriber_name = db.Column(db.String(200), nullable=True)
    email = db.Column(db.DateTime)
    password = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    
   

    def __repr__(self):
        return f'<Subscribers subscriber_number={self.subscriber_number}>'


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
