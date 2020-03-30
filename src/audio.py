import hashlib
import os
import subprocess

output_audio = True

class Audio():

    def __init__(self):
        self.cache_dir = os.path.join(os.path.dirname(__file__), 'cache')
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def speak(self, text):
        if output_audio:
            hash_object = hashlib.md5(text.encode())
            filename = os.path.join(self.cache_dir, hash_object.hexdigest()+".mp3")
            filename = os.path.join(self.cache_dir, "welcome.mp3")
            if not(os.path.isfile(filename)):
                print('not recorded yet')
            print("speaking")
            self.playsound(filename)
            print("speaking done")

        print('------ AUDIO OUTPUT ------')
        print(text)
        print('--------------------------')
        return text


    def playsound(self, filename):
        # subprocess.Popen(['mpg123', '-q', filename]).wait()
        audioDiv = ("""
            <div id="audioDiv">
            <audio controls>
                <source id="audioSource" src="{}" type="audio/mp3" />
                <p>Your browser doesn't support HTML5 audio. Here is a <a id="audioLink" href="{}">link to the audio</a> instead.</p>
            </audio>
            </div>
        """.format(filename, filename))
        return audioDiv

    def recognize_speech(self, keywords = []):
        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": "",
        }
        response["transcription"] = str(input("speech? "))
        return response
