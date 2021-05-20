from flask import Flask, render_template, redirect, request, session
import os
from twilio.rest import Client
from model import connect_to_db
import crud 


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
twilio_number = '+19414131980'

app = Flask(__name__)

###HOMEPAGE, LOGIN AND LOGOUT###

@app.route('/')
def show_homepage():
    """Show IM_melon homepage"""

    return render_template('homepage.html')

@app.route('/login', methods=["GET","POST"])
def login():
    """user login page"""

    if request.method =="POST":
        email = request.get_json().get("email_address")
        password = request.get_json().get("password")

        subscriber = crud.get_subscriber_by_email(email_address)

        if subscriber and subscriber.password == password:
            session['subscriber_number']=subscriber.subscriber_number
            return redirect('/subscriber')

    else:
        return render_template('login.html')

   
@app.route('/logout')
def logout():

    del session['subscriber_number']
    #flash("You have been logged out")

    return redirect('/')

###NEW ACCOUNT CREATION###

@app.route('/create_account', methods=["GET","POST"])
def add_new_subscriber():
    """Adding a new subscriber to database"""

    if request.method == "POST":
        name = request.get_json().get("name")
        email_address = request.get_json().get("email_address")
        phone_number = request.get_json().get("phone_number")
        password = request.get_json().get("password")
        address = request.get_json().get("address")

        new_subscriber = crud.create_subscribers(email_address, password, address, phone_number)
        #flash("You are a subscriber now! Please login")
        return redirect('/login')
    else:
        return render_template('new_account.html')

###ADDING NEW MELONS###

@app.route('/add_new_melon', methods=["GET", "POST"])
def add_new_melon():
    """Adding a new melon"""

    if request.method == "POST":
        add_new_melon_called = True
        name = request.get_json().get("name")
        qty = request.get_json().get("qty")
        mel_type = request.get_json().get("melon-type")
        mel_season = request.get_json().get("melon-season")

        new_melon = crud.create_melons(name, qty, mel_type, mel_season)

    else:
        return render_template('add_new_melon.html')


###TWILIO SMS ROUTES###
def new_melon_alert(subscriber_numbers, alert_message):
    """Sends subscribers an alert message when new melon is added"""

    subscriber_alert_numbers = crud.get_all_subscriber_numbers
    if add_new_melon_called:
        for num in subscriber_alert_numbers:
            message = client.messages \
                .create(
                     body=message,
                     from_=twilio_number,
                     to=num
                 )
            print(message.sid)
            print(message.status)




if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')