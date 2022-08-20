import pygame
RED = (196,66,38)
BLACK = (0,0,0)
WHITE = (255,255,255)

#Class that represents character 1
class Person(pygame.sprite.Sprite):
    #Call the parent class and (Sprite) constructor
    def __init__(self, color, width, height):
        super().__init__()

        #set characters image
        self.image = pygame.image.load("assets/person.png").convert_alpha()

        self.rect = self.image.get_rect()
