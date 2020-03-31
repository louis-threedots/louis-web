import louis_globals as glob
class Arduino:

    def discover(self):
        glob.mainApp.audio.speak(text="How many cells would you like to work with?", name="arduino_cells")
        return int(glob.cust_input())

    def run_to_rel_pos(self, rel_angle, cell_index):
        return

    def get_pressed_button(self):
        glob.mainApp.audio.speak(text="Enter a cell index to imitate a button press.", name="arduino_button")
        return int(glob.cust_input())

    def ping(self, cell_index):
        return True