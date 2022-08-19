import pygame
RED = (196,66,38)

#Class that represents character 1
class Person(pygame.sprite.Sprite):
    #Call the parent class and (Sprite) constructor
    def __init__(self, color, width, height):
        super().__init__()