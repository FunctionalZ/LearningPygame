import pygame

class PauseScreen(pygame.sprite.Sprite):
    #Call the parent class and (Sprite) constructor
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.image.load("assets/PauseMenu.png").convert_alpha()
            
        self.rect = self.image.get_rect()

class MenuArrow(pygame.sprite.Sprite):
    #Call the parent class and (Sprite) constructor
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.image.load("assets/Arrow.png").convert_alpha()
            
        self.rect = self.image.get_rect()

    def arrowRight(self, pixels):
        self.rect.x -= pixels
        
    def arrowLeft(self, pixels):
        self.rect.x += pixels

    def arrowDown(self, pixels):
        self.rect.y += pixels

    def arrowUp(self, pixels):
        self.rect.y -= pixels