from flask import Flask, render_template, redirect
from model import connect_to_db
#import crud

app = Flask(__name__)

@app.route('/')
def show_homepage():
    """Show IM_melon homepage"""

    return render_template('homepage.html')

@app.route('/login')
def show_login():
    """Show user login page"""

    return render_template('login.html')

@app.route('/login', methods=["POST"])
def enter_login_info():
    """Signing in, checks if user exists"""

    email = request.get_json().get("email")
    password = request.get_json().get("password")
    subscriber = crud.get_subscriber_by_email(email)
    
    if subscriber and subscriber.password == password:
        session['subscriber_id'] = subscriber.subscriber_id
        return redirect("/subscriber")


@app.route('/add_new_melon')
def show_add_melon_page():
    """Renders admin page"""
    return render_template('add_new_melon.html')

@app.route('/add_new_melon', methods=["POST"])
def update_melons_database():
    """Add new melon to database"""

    name = request.get_json().get("name")
    qty = request.get_json().get("qty")
    mel_type = request.get_json().get("melon-type")
    mel_season = request.get_json().get("melon-season")

    #new_melon = crud.create_new_melon(name, qty, mel_type, mel_season)
    #flash message

    return redirect('/homepage')

@app.route('/create_account')
def show_create_account():
    """Show new account page"""

    return render_template('new_account.html')

@app.route('/create_account', methods=["POST"])
def add_new_subscriber():
    """Adding a new subscriber to database"""

    name = request.get_json().get("name")
    email = request.get_json().get("email")
    phone_number = request.get_json().get("phone_number")
    password = request.get_json().get("password")
    address = request.get_json().get("address")
    notification = request.get_json().get("notification")
    
    #new_subscriber = crud.create_new_subscriber(name, email, password, phone_number, address, notification)

    return redirect('/login')

@app.route('/subscriber/<subscriber_name>')
def view_subscriber():
    """View subscriber page with what they have signed up for"""

    return render_template("subscriber.html")

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')