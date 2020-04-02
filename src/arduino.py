import louis_globals as glob
class Arduino:

    def discover(self):
        glob.mainApp.audio.speak("How many cells would you like to work with? (integer)")
        inp = glob.cust_input()
        try:
            return int(inp)
        except:
            return self.discover()

    def run_to_rel_pos(self, rel_angle, cell_index):
        return

    def get_pressed_button(self):
        glob.mainApp.audio.speak("Enter a cell index to imitate a button press. (integer)")
        inp = glob.cust_input()
        try:
            return int(inp)
        except:
            return self.get_pressed_button()

    def ping(self, cell_index):
        return True