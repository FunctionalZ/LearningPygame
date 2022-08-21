from tokenize import _all_string_prefixes
import pygame, time, random
from assets.character import Person
from assets.levels import Level

#engine initialize
pygame.init

#declare colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#Open game window
size = (640,480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Learning Project")

#lists that contains all sprites
player_sprites = pygame.sprite.Group()
level_sprites = pygame.sprite.Group()

#create player sprite
playerChar = Person(BLACK, 16, 16)
playerChar.rect.x = 320
playerChar.rect.y = 240

#create level sprite
levelArea = Level(BLACK, 640, 480)
levelArea.rect.x = 0
levelArea.rect.y = 0

#add player character to the list of objects
player_sprites.add(playerChar)
level_sprites.add(levelArea)

carryOn = True
clock = pygame.time.Clock()

#coordinates pre setup
coordX = 0
coordY = 0

#physics pre setup
velocity = 16
previous_time = time.time()
deltaTime = 0

while carryOn:
    #set the FPS
    clock.tick(10)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
    
    #time physics stuff
    now = time.time()
    deltaTime = now - previous_time
    prev_time = now
    
    #pressing keys does funni
    keys = pygame.key.get_pressed()
    #Logic for moving up
    if keys[pygame.K_w]:
        levelArea.moveUp(16)
        coordY = coordY + 1
        print("Y coord: " + str(coordY))
    #Logic for moving Left
    if keys[pygame.K_a]:
        levelArea.moveLeft(16)
        coordX = coordX - 1
        print("X coord: " + str(coordX))
    #Logic for moving Downward
    if keys[pygame.K_s]:
        levelArea.moveDown(16)
        coordY = coordY - 1
        print("Y coord: " + str(coordY))
    #Logic for moving Right
    if keys[pygame.K_d]:
        levelArea.moveRight(16)
        coordX = coordX + 1
        print("X coord: " + str(coordX))
    
    if keys[pygame.K_g]:
        print("debug info:")
        print("X coord: " + str(coordX))
        print("Y coord: " + str(coordY))


    #Game Logic
    player_sprites.update()
    level_sprites.update()

    #paint the screen
    screen.fill(BLACK)

    #draw sprites to screen
    level_sprites.draw(screen)
    player_sprites.draw(screen)

    #screen update
    pygame.display.flip()

pygame.quit()