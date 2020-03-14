from app import App
from characters import *

class Riddles(App):

    def on_start(self):
        self.riddles = self.get_riddles()
        self.app_instruction("This app will tell you riddles. The answer will be given in braille. It will pick up where you left off. You can browse by saying next and previous.")
        self.next_riddle()

    def next_riddle(self):
        if self.settings['riddle_idx'] >= len(self.riddles):
            self.audio.speak("Unfortunately we don't have any new riddles at the moment. We hope you enjoyed them!")
            self.settings['riddle_idx'] = 0

        riddle = self.riddles[self.settings['riddle_idx']]
        self.audio.speak(
            "Riddle number " + str(self.settings['riddle_idx'] + 1) + ": "
            + riddle['question']
        )

        self.print_text(riddle['answer'])
        self.settings['riddle_idx'] += 1

        response = self.await_response(['next', 'previous'])
        if response == "previous":
            self.settings['riddle_idx'] -= 2

        self.next_riddle()

    def get_riddles(self):
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
