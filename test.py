import pygame


pygame.init()

def readhm():
    image = pygame.image.load("Heightmap.png")
    
    colormap = [[0 for r in range(257)] for cl in range(257)]
    
    for x in range(257):
        for y in range(257):
            color = image.get_at((x,y))
            colormap[x][y] = color[0]
            
    print(colormap)
    
    
readhm()