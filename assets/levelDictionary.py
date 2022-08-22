currentLevel = 1
"""
levelWidth and levelHeight refer to the dimensions of the image that the level uses
StartX and StartY refer to the offset in x or y pixels that the level should be. For example the imaged for Level id 2 is 
moved right 192 pixels and is moved up 160 pixels 
"""

if currentLevel == 1:
    #set dimensions for level 1
    levelWidth = 256
    levelHeight = 192
    StartX = 192
    StartY = 160
    startCoords = [1,1]
    #Valid Coordinates
    validCoords = ([0,0], [0,1], [0,-1], [0,-2], [1,0], [1,1], [1,-1], [1,-2], [2,0], [2,1], [2,-1], [2,-2], 
    [3,0], [3,1], [3,-1], [3,-2], [3,2], [3,3], [2,3], [1,2], [1,3], [0,2], [0,3], [-1, 3], [-2, 3], [-3, 3], [-4, 3])