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

#create sprite
playerChar = Person(WHITE, 16, 16)
playerChar.rect.x = 100
playerChar.rect.y = 100

carryOn = True

clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
    
    #paint the screen
    screen.fill(BLACK)

    #screen update
    pygame.display.flip()
    
    #set the FPS
    clock.tick(60)
    
    
pygame.quit()