from flask import Flask, render_template, redirect, request, session, jsonify
import os
from twilio.rest import Client
from model import connect_to_db
import crud 


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
twilio_number = '+19414131980'

app = Flask(__name__)
app.secret_key = "dev"
###HOMEPAGE, LOGIN AND LOGOUT###

#@app.route('/api/login', methods=['POST']) #THIS IS THE ROUTE THAT HANDLES ADMIN LOGIN
#def login():
    #email = request.json.get('email') #thanks to that content-type header!
    #password = request.json.get('password')

    #result = None
    # DO LOGIN VALIDATION HERE MIGHT LOOK LIKE...
    # user = crud.get_user_by_email(email)
    
    # if user and user.password == password:
    #     result = {
    #         'name': user.name,
    #         'email': user.email,
    #         'user_id': user.user_id
    #         }
    # print('*' * 20)
    #result = "if it's not None it will work"

    #print(result)
    #return jsonify(result)

@app.route('/api/subscribe', methods=['POST']) #THIS IS THE ROUTE THAT HANDLES SUBSCRIBERS
def subscribe():
    name = request.json.get('name') #thanks to that content-type header!
    password = request.json.get('password')
    email = request.json.get('email')
    phone = request.json.get('phone')
    #melon_name = request.json.get('melon_name')

    add_subscriber = crud.create_subscribers(phone, name, email, password)
    # DATABASE CHECKS AND CRUD FUNCTIONS GO HERE
    # CREATE A NEW RECORD FOR THE SUBSCRIBER
    
    # RETURN SOME RESPONSE WITH SOME MESSAGE (SUCCESS/FAIL, etc)
    result = {'status': 'success'}
    return jsonify(result)



@app.route('/api/add_melon', methods=['POST']) #THIS IS THE ROUTE THAT ADDS MELONS FROM ADMIN PAGE
def add_melon():
    name = request.json.get('name')
    quantity = request.json.get('quantity') 
    melon_type = request.json.get('type')
    season = request.json.get('season')

    add_melon = crud.create_melons(name, quantity, melon_type, season)
    new_melon_alert(name, quantity)
    # subscriber_alert_numbers = crud.get_all_subscriber_numbers()
    # print(subscriber_alert_numbers)
    # for num in subscriber_alert_numbers:
    #     message = client.messages \
    #         .create(
    #         body=message,
    #         from_=twilio_number,
    #         to=num
    #             )
    #     print(message.sid)
    #     print(message.status)

    # DO YOUR TWILIO API CALL HERE (best to have that in a helper function that you call here)
    # Probably something like query for all subscribers and then loop them one by one and text them

    # RETURN SOME RESPONSE WITH SOME MESSAGE (SUCCESS/FAIL, etc)
    result = {'status': 'success'}
    return jsonify(result)



###TWILIO SMS ROUTES###
def new_melon_alert(name,quantity):
    """Sends subscribers an alert message when new melon is added"""

    subscriber_alert_numbers = crud.get_all_subscriber_numbers()
    print(subscriber_alert_numbers)
    for num in subscriber_alert_numbers:
        alert_message = client.messages \
            .create(
            body="New melon added! "+name+ " has been added, "+quantity+ " available right now.",
            from_=twilio_number,
            to=num
                )
        print(alert_message.sid)
        print(alert_message.status)

    

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

###################################################
if __name__ == "__main__":
    #connect_to_db(app) #when we are running the actual server use this db

    connect_to_db(app, "postgresql:///testdb") #when we are running the test files use this db

    app.run(debug=True, host='0.0.0.0')