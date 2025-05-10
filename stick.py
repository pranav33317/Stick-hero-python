# stick.py
from config import Config

class Stick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 0
        self.angle = 0
        self.state = "static"  # states: growing, falling, static

    def update(self):
        if self.state == "growing":
            self.length += Config.STICK_GROW_SPEED
        elif self.state == "falling":
            if self.angle < 90:
                self.angle += Config.STICK_FALL_SPEED

    def reset(self, x, y):
        self.__init__(x, y)
