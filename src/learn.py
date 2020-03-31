import louis_globals as glob
from app import App
from characters import *

class Learn(App):

    def on_start(self):
        # instruction when app started, skip when the user says skip
        self.app_instruction("Here you will learn the alphabet. You can move on to the next character by saying next.")
        self.learn_category()

    def learn_category(self):
        glob.mainApp.audio.speak("""
            Which of the following categories would you like to learn?
            The alphabet, punctuation, digits, special indicators or contractions?
        """)

        reply = self.await_response(["alphabet", "punctuation", "digits", "contractions", "indicators"])
        if "alphabet" in reply:
            glob.mainApp.audio.speak("Let's learn the lowercase alphabet.")
            learn_chars = alphabet_dict
            audio_announcement, audio_name = "This is the letter", "learn_announce_letter"
        elif "punctuation" in reply:
            glob.mainApp.audio.speak("Let's learn punctuation characters.")
            learn_chars = punctuation_dict
            audio_announcement, audio_name = "This is a", "learn_announce_punctuation"
        elif "digits" in reply:
            glob.mainApp.audio.speak("Let's learn digits.")
            learn_chars = digit_dict
            audio_announcement, audio_name = "This is the number", "learn_announce_digit"
        elif "contractions" in reply:
            glob.mainApp.audio.speak("Let's learn contractions.")
            learn_chars = contraction_dict
            audio_announcement, audio_name = "This is the contraction", "learn_announce_contraction"
        elif "indicators" in reply:
            glob.mainApp.audio.speak("Let's learn special indicators.")
            learn_chars = indicator_dict
            audio_announcement, audio_name = "This announces a", "learn_announce_indicator"

        for c in learn_chars:
            self.print_character_all_cells(c)
            glob.mainApp.audio.speak(text=audio_announcement, name=audio_name)
            glob.mainApp.audio.speak(text=character_dict[c]['display'], name=('char_'+character_dict[c]['display'].replace(' ', '_')))
            self.await_response(["next"])

        glob.mainApp.audio.speak("That were all the characters. Would you like to learn another category?")
        reply = self.await_response(["yes","no"])
        if reply == 'yes':
            self.learn_category()

        self.on_quit()
