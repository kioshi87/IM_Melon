
from model import db,  Melon, Subscriber,  connect_to_db 
import sqlalchemy

"""CRUD operations."""
def create_melons(melon_name, melon_qty,melon_type, melon_season):
    """Create and return a new melon."""
    melon = Melon(melon_name=melon_name, melon_qty=melon_qty,melon_type=melon_type, melon_season=melon_season)
    db.session.add(melon)
    db.session.commit()

    return melon

def create_subscribers(subscriber_number, name, email, password):
    """Create and return a new user."""
    subcriber= Subscriber(subscriber_number=subscriber_number, name=name,email=email, password=password)
    db.session.add(subcriber)
    db.session.commit()

    return subcriber

def get_all_subscriber_numbers():
    """List of all subscriber numbers"""

    all_subscribers = get_all_subscriber()
    phone_numbers = []
    for subscriber in all_subscribers:
        number = subscriber.subscriber_number
        phone_numbers.append(number)
    
    return phone_numbers
    
def get_all_subscriber():
    """Return all users."""
    return Subscriber.query.all()





# def get_subscriber_by_email(email):
#     """Return a user by email."""
#     return Subscribers.query.filter(Subscribers.email == email).first()




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
