# create a new melon record, new subsscriber, subscriber is in
from model import db, AlertSystem,  Melons,   Messages, Subscribers,  connect_to_db 
# from sqlalchemy.sql import func, cast
# from datetime import datetime, date
import sqlalchemy

"""CRUD operations."""
def create_melons(melon_name, melon_qty,melon_type, melon_season):
    """Create and return a new melon."""
    melon = Melons(melon_name=melon_name, melon_qty=melon_qty,melon_type=melon_type, melon_season=melon_season)
    db.session.add(melon)
    db.session.commit()

    return melon

def create_subscribers(email, password, address, subscriber_number):
    """Create and return a new user."""
    subcriber= Subscribers(email=email, password=password, address=address, subscriber_number=subscriber_number)
    db.session.add(subcriber)
    db.session.commit()

    return subcriber

def create_alert(id, melon_name, subscriber_number, message_id):
    alert = AlertSystem(id=id, melon_name=melon_name, subscriber_number=subscriber_number, message_id=message_id)
    db.session.add(alert)
    db.session.commit()

def create_messages( subscriber_number, melon_name, qty_alert, type_alert, season_alert):
    message= AlertSystem(melon_name=melon_name, subscriber_number=subscriber_number, season_alert=season_alert, qty_alert=qty_alert, type_alert=type_alert)
    db.session.add(message)
    db.session.commit()

def get_all_subscriber():
    """Return all users."""
    return Subscribers.query.all()

def get_all_subscriber_numbers():
    """List of all subscriber numbers"""

    all_subscribers = get_all_subscriber()
    phone_numbers = []
    for subscriber in all_subscribers:
        number = subscriber.subscriber_number
        phone_numbers.append(number)
    
    return phone_numbers 

def get_subscriber_by_number(subscriber_number):
    """Return a user by number."""
    return Subscribers.query.get(subscriber_number)

def get_subscriber_by_email(email):
    """Return a user by email."""
    return Subscribers.query.filter(Subscribers.email == email).first()

def get_all_alerts():
    """Return all alerts"""
    return AlertSystem.query.all()

def get_alerts_by_melon_name(melon_name):
    """Return alert by melon type"""
    return Melons.query.filter(Melons.melon_name == melon_name).first()

def get_messages_quantity(quantity_alert):
    """Return message by quantity"""
    return Messages.query.filter(Melons.quantity_alert== quantity_alert).first()

def get_messages_type(type_alert):
    """Return message by type"""
    return Messages.query.filter(Melons.type_alert== type_alert).first()

def get_messages_season(season_alert):
    """Return message by season"""
    return Messages.query.filter(Melons.season_alert== season_alert).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
