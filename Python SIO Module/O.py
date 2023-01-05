import requests
from twilio.rest import Client
from jaseci.actions.live_actions import jaseci_action  # step 1

account_sid = 'ACee822b0413f5082a689a80dd3b966328' 
auth_token = '68d2580abca094db45be410317f3aaf4'
client = Client(account_sid, auth_token) 



@jaseci_action(act_group=["O"], allow_remote=True)

def send_media(media, phone_number):
    ngrok_webhook = "https://63a7-2800-3c0-2050-d1-3d1a-ac46-8151-448b.sa.ngrok.io/"
    user_media = ngrok_webhook+media
    if media:
        messagess = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    media_url=user_media,
                                    to=phone_number
                                ) 
    return messagess
