import os
from twilio.rest import Client
#import crud

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
twilio_number = '+19414131980' 

#### TWILIO SMS ROUTES ####
def new_melon_alert():

    """Sends subscribers an alert message when new melon is added"""

    for num in subscriber_alert_numbers:
        alert_message = client.messages \
                .create(
                     body="New melon added!",
                     from_=twilio_number,
                     to=num
                 )
        print(alert_message.sid)
        print(alert_message.status)

# message = "New melon added!"
# new_melon_alert(subscriber_alert_numbers, message)