currentLevel = 2

if currentLevel == 1:
    #set dimensions for level 1
    levelWidth = 640
    levelHeight = 480
    StartX = 0
    StartY = 0
    

if currentLevel == 2:
    #set dimensions for level 2
    levelWidth = 256
    levelHeight = 192
    StartX = 192
    StartY = 160
    #Valid Coordinates
    validCoords = ([0,0], [0,1], [0,-1], [0,-2], [1,0], [1,1], [1,-1], [1,-2], [2,0], [2,1], [2,-1], [2,-2], 
    [3,0], [3,1], [3,-1], [3,-2], [3,2], [3,3], [2,3], [1,2], [1,3], [0,2], [0,3], [-1, 3], [-2, 3], [-3, 3], [-4, 3])