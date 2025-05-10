# game_view.py
import pygame
from config import Config
from game_manager import GameManager

class GameView:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Stick Hero")
        self.font = pygame.font.Font(None, 36)

    def draw_text(self, text, position):
        text_surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surface, position)

    def render(self):
        self.screen.fill(Config.BG_COLOR)
        manager = GameManager()
        
        # Draw platforms
        for platform in manager.platforms:
            pygame.draw.rect(self.screen, Config.PLATFORM_COLOR,
                           (platform.x, 400, platform.width, 20))
            
        # Draw stick
        stick = manager.stick
        end_x = stick.x + stick.length * pygame.math.Vector2(0, -1).rotate(stick.angle).x
        end_y = 400 - stick.length * pygame.math.Vector2(0, -1).rotate(stick.angle).y
        pygame.draw.line(self.screen, Config.STICK_COLOR,
                        (stick.x, 400), (end_x, end_y), 5)
        
        # Draw player
        pygame.draw.rect(self.screen, Config.PLAYER_COLOR,
                        (manager.player.x - 15, manager.player.y - 30, 30, 30))
        
        # Draw score
        self.draw_text(f"Score: {manager.score}", (10, 10))
        
        if manager.game_over:
            self.draw_text("Game Over! Press SPACE to restart", 
                          (Config.WIDTH//2 - 180, Config.HEIGHT//2))
        
        pygame.display.flip()
