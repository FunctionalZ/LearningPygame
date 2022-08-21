from distutils.dist import DistributionMetadata
from sys import displayhook
from tokenize import _all_string_prefixes
import pygame, time, random
from assets.character import Person
from assets.levelList import Level
from assets.levelDictionary import currentLevel
from assets.levelDictionary import levelWidth
from assets.levelDictionary import levelHeight
from assets.levelDictionary import StartX
from assets.levelDictionary import StartY
from assets.levelDictionary import validCoords

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
playerChar = Person(BLACK, 32, 32)
playerChar.rect.x = 320
playerChar.rect.y = 256

#create level sprite
levelArea = Level(BLACK, levelWidth, levelHeight)
levelArea.rect.x = StartX
levelArea.rect.y = StartY

#add player character to the list of objects
player_sprites.add(playerChar)
level_sprites.add(levelArea)

carryOn = True
clock = pygame.time.Clock()

coordinates = [0, 0]
coordinateForcast = [0,0]

while carryOn:
    #set the FPS
    clock.tick(10)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
    
    #pressing keys does funni
    keys = pygame.key.get_pressed()
    #Logic for moving up needs to be fixed so that valid coordinates are properly identified and then compared to this code
    """
    if keys[pygame.K_w]:
        coordinateForcast[1] = coordinateForcast[1] + 1
        for i in range(len(validCoords)):
            if validCoords[i] == coordinateForcast:
                print(i)
                print(validCoords[i])
                levelArea.moveUp(32)
                coordinates[1] = coordinates[1] + 1
    """
    #Logic for moving Left
    if keys[pygame.K_a]:
            levelArea.moveLeft(32)
            coordinates[0] = coordinates[0] - 1
            coordinateForcast = coordinates
    #Logic for moving Downward
    if keys[pygame.K_s]:
        levelArea.moveDown(32)
        coordinates[1] = coordinates[1] - 1
        coordinateForcast = coordinates
    #Logic for moving Right
    if keys[pygame.K_d]:
        levelArea.moveRight(32)
        coordinates[0] = coordinates[0] + 1
        coordinateForcast = coordinates
    
    if keys[pygame.K_g]:
        print("debug info:")
        print("Coordinates: " + str(coordinates))
        print("Coordinate Forecast: " + str(coordinateForcast))

    #Game Logic
    coordinateForcast = coordinates
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