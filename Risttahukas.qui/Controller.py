from tkinter import simpledialog
from Model import Model
from View import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def new_game_click(self):
        self.model.start_new_game()
        self.view.btn_new_game["state"] = "normal"
        self.view.height_entry["state"] = "normal"
        self.view.length_entry["state"] = "normal"
        self.view.width_entry["state"] ="normal"
        self.view.btn_send["state"] = "normal"

    def send_click(self, event=None):
        try:
            height = float(self.view.height_entry.get())
            length = float(self.view.length_entry.get())
            width = float(self.view.width_entry.get())
        except ValueError:
            self.view.display_results("Palun sisesta kõik numbrilised väärtused.")
            return

        diameter = self.model.calculate_diameter(height, length, width)
        surface_area = self.model.calculate_surface_area(height, length, width)
        volume = self.model.calculate_volume(height, length, width)

        result_text = f"Diameeter: {diameter}\nTäispindala: {surface_area}\nRuumala: {volume}"
        self.view.display_results(result_text)

        if self.model.game_over:
            self.view.btn_new_game["state"] = "disabled"
            self.view.height_entry["state"] = "disabled"
            self.view.length_entry["state"] = "disabled"
            self.view.width_entry["state"] = "disabled"
            self.view.btn_send["state"] = "disabled"
