import requests
import urllib.request
from jaseci.actions.live_actions import jaseci_action  # step 1

account_sid = 'ACee822b0413f5082a689a80dd3b966328' 
auth_token = '68d2580abca094db45be410317f3aaf4'

@jaseci_action(act_group=["I"], allow_remote=True)

def get_media(image_url, audio_url, file_name):
    if image_url:
        urllib.request.urlretrieve(image_url, file_name)

    if audio_url:
        response = requests.get(audio_url, auth=(account_sid, auth_token))
        with open(file_name, 'wb') as f:
            f.write(response.content)




# send_media("media.mp3", 'whatsapp:+5926136206')
image = "https://i.ytimg.com/vi/G68oSgFotZA/maxresdefault.jpg"
file_name = "1111111111111111111111.jpg"
get_media(image, None, file_name)
audio_url = "https://api.twilio.com/2010-04-01/Accounts/ACee822b0413f5082a689a80dd3b966328/Messages/MM9851f61a3a0b55df4fbf742f413a5f09/Media/ME6487161e92ff32d0819030c84d48847d"
file_name = "1111111111111111111.mp3"
get_media(None, audio_url, file_name)
