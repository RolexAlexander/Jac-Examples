from gtts import gTTS
from jaseci.actions.live_actions import jaseci_action

@jaseci_action(act_group=["Speak"], allow_remote=True)

def speech(user_text, file_name):
    language = 'en'
    speech = gTTS(text=user_text, lang=language, slow=False)

    # Save the speech as an MP3 file:
    speech.save(file_name)
