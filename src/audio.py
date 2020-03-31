import louis_globals as glob
import os
import subprocess

output_audio = True

class Audio():

    def __init__(self):
        # conversion from Google Drive sharing URL to Google Drive Direct Link: https://www.wonderplugin.com/online-tools/google-drive-direct-link-generator/
        self.audioFiles = {# name: direct link
            "main_welcome": "https://drive.google.com/uc?export=download&id=1VTikh68z4lV72lxrG-0Gj_RJlOMOdYYh",
            "main_open_apps": "https://drive.google.com/uc?export=download&id=1FQ9uJKHhu2l9n_60IPANWguzP78wnMSn"
        }

    def speak(self, text="", name=""):
        
        print('------ AUDIO OUTPUT ------')
        glob.cust_print(text)
        print('--------------------------')

        if output_audio:
            if name not in self.audioFiles:
                glob.cust_print('(There is no audio recording yet.)')
            else:
                print("speaking")
                self.playsound(self.audioFiles[name])
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
