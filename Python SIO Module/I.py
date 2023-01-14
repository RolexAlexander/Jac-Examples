import requests
import urllib.request
from jaseci.actions.live_actions import jaseci_action  # step 1

headers = {
    "Authorization": "Bearer EAAuwHrSFCigBAIHOXqlqlhZClIjqbLQ5Q93eQMUPAStZB9eu6BVA2EmGWNRAnSRxXjiWBbodaEnppC7ZCP1uVStLFTMNOZBhaj5ZAWogSWSsfkZB1ayjtKQE1vK4qXnhRbwA05ZCg8I1dZCZCzDJQWJrZA9Chna7PeZCzgz9riWSFjGoqchjAP9GdfMZC07dRcR4czlVQvRMvIK4IAZDZD",
    "Content-Type": "application/json"
}

@jaseci_action(act_group=["I"], allow_remote=True)

def get_media(image_id, audio_id, file_name):
    if image_id:
        urllib.request.urlretrieve(image_id, file_name)

    if audio_id:
        url = "https://graph.facebook.com/v15.0/"+audio_id+"?phone_number_id=100744942921876"
        response = requests.get(url, headers=headers)
        print(response.json())
        data = response.json()
        audio_url = data["url"]
        response = requests.get(audio_url, headers=headers)
        with open(file_name, 'wb') as f:
            f.write(response.content)

get_media(None, "865104201303257", "user_utterance.mp3")