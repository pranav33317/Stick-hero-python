# game_manager.py
from player import Player
from stick import Stick
from platform import Platform

class GameManager:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls.reset()
        return cls._instance
    
    @classmethod
    def reset(cls):
        cls.score = 0
        cls.platforms = [
            Platform(200, 150),
            Platform(600, 150)
        ]
        cls.player = Player(200, 400)
        cls.stick = Stick(200, 400)
        cls.game_active = True
        cls.game_over = False
