#!/usr/bin/env python
# Install the Python helper library from twilio.com/docs/python/install

from twilio.rest import Client

ACCOUNT_SID = 'ACd6a50ee590d5815ab0258eca55ba0e31'
AUTH_TOKEN = 'bd611cc3851e324c01db521769f2dd46'
#TWILIO_PHONE_NUMBER = '+17692308547' -- We dont need as the 
MY_PHONE_NUMBER = '+15852378764'
client = Client(ACCOUNT_SID, AUTH_TOKEN)

#!/usr/bin/env python
# Install the Python helper library from twilio.com/docs/python/install


# notification = client.notify.services('IS2ba0d5a87561950513b7dc5617ae94de') \
#     .notifications.create(
#         to_binding='{"binding_type":"sms", "address":"+15852378764"}',
#         body='Knok-Knok! This is your first Notify SMS')
# print(notification.sid)


# def send_sms_alert():
#     notification = client.notify.services('IS2ba0d5a87561950513b7dc5617ae94de') \
#     .notifications.create(
#         to_binding='{"binding_type":"sms", "address":{MY_PHONE_NUMBER}}',
#         body='Knok-Knok! This is your first Notify SMS')
#     print(notification.sid)
#     return notification.sid

def send_sms_alert_new_melon(newmelon_body):
    notification = client.notify.services('IS2ba0d5a87561950513b7dc5617ae94de') \
    .notifications.create(
        to_binding='{"binding_type":"sms", "address":"+15852378764"}',
        body = newmelon_body)
    print(notification.sid)
    return notification.sid