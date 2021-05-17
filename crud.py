# create a new melon record, new subsscriber, subscriber is in
from model import db, AlertSystem,  Melons,   Messages, Subscribers,  connect_to_db 


"""CRUD operations."""

def create_user(email, password):
    """Create and return a new user."""

    user = Subscribers(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_alert(id, melon_name, subscriber_number, message_id):
    alert = AlertSystem(id=id, melon_name=melon_name, subscriber_number=subscriber_number, message_id=message_id)
    db.session.add(alert)
    db.session.commit()

def get_users():
    """Return all users."""

    return Subscribers.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""
    return Subscribers.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""
    return Subscribers.query.filter(Subscribers.email == email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
