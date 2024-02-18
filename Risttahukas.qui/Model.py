import math

class Model:
    def __init__(self):
        self.game_over = False

    def start_new_game(self):
        self.game_over = False

    def calculate_diagonal(self, height, length, width):
        # Arvutused diagonaali jaoks
        diagonal = math.sqrt(length ** 2 + width ** 2 + height ** 2)
        return diagonal

    def calculate_surface_area(self, height, length, width):
        # Arvutused täispinna jaoks
        surface_area = 2 * (length * width + width * height + length * height)
        return surface_area

    def calculate_volume(self, height, length, width):
        # Arvutused ruumala jaoks
        volume = length * width * height
        return volume