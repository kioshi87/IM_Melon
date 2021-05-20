import os
from twilio.rest import Client
#import crud

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
twilio_number = '+19414131980' 
message = "New melon added!"
#### TWILIO SMS ROUTES ####
def new_melon_alert(subscriber_numbers, alert_message):

    """Sends subscribers an alert message when new melon is added"""

    for num in subscriber_numbers:
        message = client.messages \
                .create(
                     body=message,
                     from_=twilio_number,
                     to=num
                 )
        print(message.sid)
        print(message.status)


