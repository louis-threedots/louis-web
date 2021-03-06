import louis_globals as glob
from app import App

class Riddles(App):

    def on_start(self):
        self.riddles = self.get_riddles()
        self.instruction = """
            Welcome to Riddles.
            This app will tell you riddles.
            The answer will be given in braille.
            It will pick up where you left off.
            You can browse by saying next, previous and again.
        """
        glob.mainApp.audio.speak("We are finding the most recently browsed new riddle.")
        self.next_riddle()

    def next_riddle(self):
        if self.settings['riddle_idx'] >= len(self.riddles):
            glob.mainApp.audio.speak("Unfortunately we don't have any new riddles at the moment. We hope you enjoyed them!")
            self.settings['riddle_idx'] = 0

        riddle = self.riddles[self.settings['riddle_idx']]
        glob.mainApp.audio.speak("Riddle number:")
        glob.mainApp.audio.speak(str(self.settings['riddle_idx'] + 1))
        glob.mainApp.audio.speak(riddle['question'])

        self.print_text(riddle['answer'])
        glob.mainApp.audio.speak("That was the answer.")
        self.settings['riddle_idx'] += 1

        response = self.await_response(['next', 'previous', 'again'])
        if response == "previous":
            if self.settings['riddle_idx'] - 2 < 0:
                glob.mainApp.audio.speak("There are no previous riddles. We will instead tell you the last riddle in the library.")
                self.settings['riddle_idx'] = len(self.riddles) - 1
            else:
                self.settings['riddle_idx'] -= 2
        elif response == 'again':
            self.settings['riddle_idx'] -= 1

        self.next_riddle()

    def get_riddles(self):
        # SOURCE: https://www.royalblind.org/sites/www.royalblind.org/files/Braille%20Riddles%202.pdf
        return [
            {
                "question": "Who succeeded the first Prime Minister of Great Britain?",
                "answer": "the second one"
            },
            {
                "question": "Where was the Magna Carta signed?",
                "answer": "at the bottom"
            },
            {
                "question": "What stories do the ship captain's children like to hear?",
                "answer": "ferry tales"
            },
            {
                "question": "What kind of car does Mickey Mouse's wife drive?",
                "answer": "a minnie van"
            },
            {
                "question": "What holds the moon up?",
                "answer": "moon beams"
            },
            {
                "question": "Why did the spider cross the computer?",
                "answer": "to get to his website"
            },
            {
                "question": "What kind of ship never sinks?",
                "answer": "friendship"
            },
            {
                "question": "Who writes invisible books?",
                "answer": "a ghost writer"
            },
            {
                "question": "Why does my teacher remind me of history?",
                "answer": "she is always repeating herself"
            },
        ]
