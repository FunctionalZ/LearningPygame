from tokenize import _all_string_prefixes
import pygame
from character import Person

#engine initialize
pygame.init

#declare colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#Open game window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FunctZii First Game")

#list that contains all sprites
all_sprites_list = pygame.sprite.Group()

#create sprite
playerChar = Person(BLACK, 16, 16)
playerChar.rect.x = 0
playerChar.rect.y = 0

#add player character to the list of objects
all_sprites_list.add(playerChar)

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
    
    #Game Logic
    all_sprites_list.update()

    #paint the screen
    screen.fill(BLACK)

    #draw sprites to screen
    all_sprites_list.draw(screen)

    #screen update
    pygame.display.flip()
    
    #set the FPS
    clock.tick(60)
    
    
pygame.quit()