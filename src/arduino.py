class Arduino:

    def __init__(self):
        self.main_cell = 'comp'

    def discover(self):
        return int(input("number of cells? "))

    def run_to_rel_pos(self, rel_angle, cell_index):
        return

    def get_pressed_button(self):
        x = int(input("> Enter cell index to imitate button press: "))
        return x

    def ping(self, cell_index):
        return True