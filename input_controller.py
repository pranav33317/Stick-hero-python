# input_controller.py
from game_manager import GameManager

class InputController:
    def handle_input(self):
        manager = GameManager()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if manager.game_active:
                        manager.stick.state = "growing"
                    else:
                        GameManager.reset()
                        manager.game_active = True
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and manager.game_active:
                    manager.stick.state = "falling"
                    self.handle_stick_drop()

    def handle_stick_drop(self):
        manager = GameManager()
        current_platform = manager.platforms[0]
        required_length = manager.platforms[1].x - (current_platform.x + current_platform.width)
        
        if manager.stick.length >= required_length:
            manager.player.state = "moving"
        else:
            manager.player.state = "falling"
