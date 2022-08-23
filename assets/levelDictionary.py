currentLevel = 1
StartX = 0
StartY = 0
levelBoundsFill = (0,0,0)

"""
levelWidth and levelHeight refer to the dimensions of the image that the level uses
StartX and StartY refer to the offset in x or y pixels that the level should be. For example the imaged for Level id 2 is 
moved right 192 pixels and is moved up 160 pixels 
"""

if currentLevel == 1:
    #set dimensions for level 1
    levelWidth = 256
    levelHeight = 192
    startCoords = [-4,6]
    levelBoundsFill = [98,98,98]
    #Valid Coordinates
    validCoords = ([-3,3],[-3,4],[-3,5],[-3,6],[-3,7],[-3,8],[-4,3],[-4,4],[-4,5],[-4,6],[-4,8],
    [-5,3],[-5,4],[-5,5],[-5,6],[-5,7],[-5,8],[-6,3],[-6,4],[-6,5],[-6,6],[-6,7],[-6,8],[-7,8],[-8,8],[-9,8],[-10,8])