# player.py
from config import Config

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "idle"
        self.velocity = 0

    def update(self):
        if self.state == "falling":
            self.velocity += Config.GRAVITY
            self.y += self.velocity
            if self.y > Config.HEIGHT:
                GameManager().game_over = True

    def move_to_target(self, target_x):
        if self.x < target_x:
            self.x += Config.PLAYER_SPEED
        else:
            self.state = "idle"
            GameManager().score += 1
