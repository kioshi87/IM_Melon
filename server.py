from flask import Flask, render_template, redirect
from model import connect_to_db
import crud

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

    email_address = request.get_json().get("email_address")
    password = request.get_json().get("password")
    
    if subscriber and subscriber.password == password:
        session['subscriber_number'] = subscriber.subscriber_number


@app.route('/update_database')
def show_admin_page():
    """Renders admin page"""
    return render_template('update_database.html')

@app.route('/update_database', methods=["POST"])
def update_melons_database():
    """Admin can now update database"""

@app.route('/create_account')
def show_create_account():
    """Show new account page"""

    return render_template('new_account.html')

@app.route('/create_account', methods=["POST"])
def add_new_subscriber():
    """Adding a new subscriber to database"""

    name = request.get_json().get("name")
    email_address = request.get_json().get("email_address")
    phone_number = request.get_json().get("phone_number")
    password = request.get_json().get("password")
    #check if user exists

    return redirect('/login')

@app.route('/subscriber/<subscriber_name>')
def view_subscriber():
    """View subscriber page with what they have signed up for"""

    return render_template("subscriber.html")

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')