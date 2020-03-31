import louis_globals as glob
import os
from hashlib import md5

output_audio = True

class Audio():

    def __init__(self):
        # conversion from Google Drive sharing URL to Google Drive Direct Link: https://www.wonderplugin.com/online-tools/google-drive-direct-link-generator/
        self.audioFiles = {# hashed text: direct link
            "a4d2555256766c278a8e127452489658": "https://drive.google.com/uc?export=download&id=1VTikh68z4lV72lxrG-0Gj_RJlOMOdYYh",
            "f54c5c9d7a3da333472e691f437f6ef8": "https://drive.google.com/uc?export=download&id=1FQ9uJKHhu2l9n_60IPANWguzP78wnMSn"
        }

    def speak(self, text):
        
        print('------ AUDIO OUTPUT ------')
        glob.cust_print(text)
        print('--------------------------')

        text_hashed = md5(text.encode('utf-8')).hexdigest()

        if output_audio:
            if text_hashed not in self.audioFiles:
                glob.cust_print('(There is no audio recording yet.)')
            else:
                print("speaking")
                self.playsound(self.audioFiles[text_hashed])
                print("speaking done")

        return text


    def playsound(self, filesrc):
        audioDiv = ("""
            <div id="audioDiv">
            <audio controls>
                <source id="audioSource" src="{}" type="audio/mp3" />
                <p>Your browser doesn't support HTML5 audio. Here is a <a id="audioLink" href="{}">link to the audio</a> instead.</p>
            </audio>
            </div>
        """.format(filesrc, filesrc))
        glob.cust_print(audioDiv)
        return audioDiv

    def recognize_speech(self):
        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": "",
        }
        response["transcription"] = str(glob.cust_input())
        return response
