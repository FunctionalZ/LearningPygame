# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 22:52:53 2022

@author: funct
"""
import pygame
import gamesprites

#engine initialize
pygame.init

#declare colors
BLACK = (0,0,0)
RED = (196,66,38)
WHITE = (255,255,255)

#Open game window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FunctZii First Game")

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