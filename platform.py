# platform.py
import random

class Platform:
    def __init__(self, x, width):
        self.x = x
        self.width = width
        self.gap = random.randint(150, 250)

    @classmethod
    def generate_new(cls):
        last_platform = GameManager().platforms[-1]
        new_x = last_platform.x + last_platform.width + last_platform.gap
        return Platform(new_x, 150)
