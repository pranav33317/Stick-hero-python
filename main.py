# main.py
import pygame
from config import Config
from game_manager import GameManager
from input_controller import InputController
from game_view import GameView

def main():
    view = GameView()
    controller = InputController()
    clock = pygame.time.Clock()
    
    while True:
        controller.handle_input()
        manager = GameManager()
        
        if manager.game_active:
            # Update game objects
            manager.stick.update()
            manager.player.update()
            
            # Check player movement
            if manager.player.state == "moving":
                target_x = manager.platforms[1].x + 75
                manager.player.move_to_target(target_x)
                
                # Generate new platform when player crosses
                if manager.player.x > Config.WIDTH//2:
                    manager.platforms.pop(0)
                    manager.platforms.append(Platform.generate_new())
                    manager.stick.reset(manager.platforms[0].x + 150, 400)
                    
            # Check game over condition
            if manager.game_over:
                manager.game_active = False
        
        view.render()
        clock.tick(Config.FPS)

if __name__ == "__main__":
    main()
