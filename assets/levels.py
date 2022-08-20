import pygame
BLACK = (0,0,0)

#Class that represents the first level
class Level(pygame.sprite.Sprite):
    #Call the parent class and (Sprite) constructor
    def __init__(self, color, width, height):
        super().__init__()

        #set characters image
        self.image = pygame.image.load("assets/levelOne.png").convert_alpha()

        self.rect = self.image.get_rect()
    
    def moveRight(self, pixels):
        self.rect.x - pixels
        
    def moveLeft(self, pixels):
        self.rect.x + pixels

    def moveUp(self, pixels):
        self.rect.y + pixels

    def moveDown(self, pixels):
        self.rect.y - pixels