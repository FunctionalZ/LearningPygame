from distutils.dist import DistributionMetadata
from sys import displayhook
from tokenize import _all_string_prefixes
import pygame, time, random
from assets.character import Person
from assets.levelList import Level
from assets.levelDictionary import currentLevel
from assets.levelDictionary import levelWidth
from assets.levelDictionary import levelHeight
from assets.levelDictionary import validCoords
from assets.levelDictionary import startCoords

#engine initialize
pygame.init

#declare colors
BLACK = (0,0,0)
WHITE = (255,255,255)
programIcon = pygame.image.load("assets/playerCharacter.png")

#Open game window
size = (640,480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RPG Engine (indev)")
pygame.display.set_icon(programIcon)

#lists that contains all sprites
player_sprites = pygame.sprite.Group()
level_sprites = pygame.sprite.Group()

#create player sprite
playerChar = Person(BLACK, 32, 32)
playerChar.rect.x = 320
playerChar.rect.y = 256

#create level sprite
levelArea = Level(BLACK, levelWidth, levelHeight)
levelArea.rect.x = 0
levelArea.rect.y = 0

#add player character to the list of objects
player_sprites.add(playerChar)
level_sprites.add(levelArea)

carryOn = True
clock = pygame.time.Clock()

#set everything all coordinates to 0, 0 before the game handles and makes changes to them
coordinates = [0, 0]
coordinateForcastUp = [0, 0]
coordinateForcastDown = [0, 0]
coordinateForcastLeft = [0, 0]
coordinateForcastRight = [0, 0]

#set the coordinates to the coordinates that you should start a level in
levelArea.rect.x = levelArea.rect.x - (startCoords[0] * 32)
levelArea.rect.y = levelArea.rect.y + (startCoords[1] * 32)
coordinates = startCoords

#set a flag that gets used later in code
breakFlag = False

while carryOn:
    #set the FPS
    clock.tick(10)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
    
    #coordinate forecast up
    coordinateForcastUp[0] = coordinates[0]
    coordinateForcastUp[1] = coordinates[1] + 1

    #coordinate forecast down
    coordinateForcastDown[0] = coordinates[0]
    coordinateForcastDown[1] = coordinates[1] - 1

    #coordinate forecast left
    coordinateForcastLeft[0] = coordinates[0] - 1
    coordinateForcastLeft[1] = coordinates[1]

    #coordinate forecast right
    coordinateForcastRight[0] = coordinates[0] + 1
    coordinateForcastRight[1] = coordinates[1]

    #pressing keys does funni
    keys = pygame.key.get_pressed()
    #Logic for moving up
    if keys[pygame.K_w]:
        for i in range(len(validCoords)):
            if validCoords[i] == coordinateForcastUp:
                levelArea.moveUp(32)
                coordinates[1] = coordinates[1] + 1
                breakFlag = True
            if breakFlag:
                breakFlag = False
                break       
    #Logic for moving Left
    elif keys[pygame.K_a]:
        for i in range(len(validCoords)):
            if validCoords[i] == coordinateForcastLeft:
                levelArea.moveLeft(32)
                coordinates[0] = coordinates[0] - 1
                breakFlag = True
            if breakFlag:
                breakFlag = False
                break
    #Logic for moving Downward
    elif keys[pygame.K_s]:
        for i in range(len(validCoords)):
            if validCoords[i] == coordinateForcastDown:
                levelArea.moveDown(32)
                coordinates[1] = coordinates[1] - 1
                breakFlag = True
            if breakFlag:
                breakFlag = False
                break
    #Logic for moving Right
    elif keys[pygame.K_d]:
        for i in range(len(validCoords)):
            if validCoords[i] == coordinateForcastRight:
                levelArea.moveRight(32)
                coordinates[0] = coordinates[0] + 1
                breakFlag = True
            if breakFlag:
                breakFlag = False
                break
    
    #movement keys for when you need to make a list of valid coordinates on a new map
    if keys[pygame.K_UP]:
        levelArea.moveUp(32)
        coordinates[1] = coordinates[1] + 1
    elif keys[pygame.K_LEFT]:
        levelArea.moveLeft(32)
        coordinates[0] = coordinates[0] - 1
    elif keys[pygame.K_DOWN]:
        levelArea.moveDown(32)
        coordinates[1] = coordinates[1] - 1
    elif keys[pygame.K_RIGHT]:
        levelArea.moveRight(32)
        coordinates[0] = coordinates[0] + 1

    #debug key set to g you can completely delete this section for final release
    if keys[pygame.K_g]:
        print(" ")
        print("debug info:")
        print("Coordinates: " + str(coordinates))
        print("Coordinate Forecast up: " + str(coordinateForcastUp))
        print("Coordinate Forecast down: " + str(coordinateForcastDown))
        print("Coordinate Forecast left: " + str(coordinateForcastLeft))
        print("Coordinate Forecast right: " + str(coordinateForcastRight))

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