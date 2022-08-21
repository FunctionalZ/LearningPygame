import pygame
from assets.levelDictionary import currentLevel
BLACK = (0,0,0)

#Class that represents the game's levels
class Level(pygame.sprite.Sprite):
    #Call the parent class and (Sprite) constructor
    def __init__(self, color, width, height):
        super().__init__()

        if currentLevel == 1:
            #set level image to level 1
            self.image = pygame.image.load("assets/levelOne.png").convert_alpha()

            self.rect = self.image.get_rect()
        if currentLevel == 2:
            #set level image to level 2
            self.image = pygame.image.load("assets/StoneMap.png").convert_alpha()

            self.rect = self.image.get_rect()
    
    def moveRight(self, pixels):
        self.rect.x -= pixels
        
    def moveLeft(self, pixels):
        self.rect.x += pixels

    def moveUp(self, pixels):
        self.rect.y += pixels

    def moveDown(self, pixels):
        self.rect.y -= pixels