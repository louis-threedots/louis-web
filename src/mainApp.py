#! /usr/bin/python3
from arduino import Arduino
from audio import Audio
from cell import Cell
import louis_globals as glob
import sys
from app import App

#apps
from riddles import Riddles
from learn import Learn
from tutor import Tutor
from headlines import Headlines
from memory import Memory

class MainApp(App):

    def __init__(self):
        self.apps = ['riddles', 'learn', 'tutor', 'headlines', 'memory']

    def on_start(self):
        self.audio = Audio()
        self.arduino, self.cells = self.discover()
        self.audio.speak("Welcome to Louis the brailliant assistant.")
        self.main_menu()
    
    def on_quit(self):
        sys.exit()
    
    def discover(self):
        print("Louis has started. Running cell discovery ...")
        arduino = Arduino()
        num_cells = arduino.discover()
        print(num_cells)
        cells = [Cell(i) for i in range(1,num_cells+1)]
        print("Cell discovery completed. "+str(num_cells)+" cells found.")
        return arduino, cells

    def main_menu(self):
        glob.mainApp.audio.speak("You can now open any application using voice commands.")
        print("Listening ...")
        response = self.await_response(["open "+appname for appname in self.apps])
        _, _, app_name = response.partition("open")
        self.open_app(app_name)

    def open_app(self, app_name):
        current_app = None

        app_name = app_name.replace(" ", "")
        if app_name == 'riddles':
            current_app = Riddles("Riddles")
        elif app_name == 'learn':
            current_app = Learn("Learn")
        elif app_name == 'tutor':
            current_app = Tutor("Tutor")
        elif app_name == 'headlines':
            current_app = Headlines("Headlines")
        elif app_name == 'memory':
            current_app = Memory("Memory")

        if current_app is not None:
            glob.mainApp.audio.speak("Opening the application")
            glob.mainApp.audio.speak(app_name)
            current_app.on_start()
        else: # shouldn't occur
            glob.mainApp.audio.speak("I did not recognize the app. Could you try to open the app again?")
