import louis_globals as glob
class Arduino:

    def discover(self):
        glob.mainApp.audio.speak("How many cells would you like to work with?")
        return int(glob.cust_input())

    def run_to_rel_pos(self, rel_angle, cell_index):
        return

    def get_pressed_button(self):
        glob.mainApp.audio.speak("Enter a cell index to imitate a button press.")
        return int(glob.cust_input())

    def ping(self, cell_index):
        return True