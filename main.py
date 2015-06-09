import pygame, sys, math, random

##-----------CLASSES--------------------
        


##-----------FUNCTIONS------------------
def firstgen(mapheight,mapwidth):
    
    tilemap[int(mapheight/2)][int(mapwidth/2)] = random.randint(1,255)
    
def readhm():
    image = pygame.image.load("leaves.jpg")
    
    colormap = [[0 for r in range(256)] for cl in range(256)]
    
    for x in range(256):
        for y in range(256):
            color = image.get_at((x,y))
            colormap[y][x] = color[0]
            
    return colormap




pygame.init()

WATER = 0
SAND  = 1
GRASS = 3
MOSS  = 4
ROCK  = 5

tiletextures = {
                WATER  : pygame.image.load("water.png"),
                SAND   : pygame.image.load("sand.png"),
                GRASS  : pygame.image.load("grass.png"),
                MOSS   : pygame.image.load("heightgrass.png"),
                ROCK   : pygame.image.load("rock.png")
                }

tilesize = 4
mapwidth = 256
mapheight = 256

tiles = [WATER,SAND,GRASS,MOSS,ROCK]
tilemap = readhm()

background = pygame.Surface((mapwidth*tilesize,mapwidth*tilesize))

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
clock = pygame.time.Clock()

for i in range(256):
    for j in range(256):
        if tilemap[i][j] <= 50:
            tile = WATER
        elif tilemap[i][j] <= 60:
            tile = SAND
        elif tilemap[i][j] <= 160:
            tile = GRASS
        elif tilemap[i][j] <= 220:
            tile = MOSS
        else:
            tile = ROCK
        
        tilemap[i][j] = tile






mainloop = True
while mainloop:
    pygame.display.set_caption('fps:%f'%clock.get_fps())
    clock.tick(60)

    #event loop
    for event in pygame.event.get():
        ##print(event)
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop=False
                pygame.quit()
                sys.exit()
                
    for row in range(mapheight):
        for column in range (mapwidth):
            background.blit(tiletextures[tilemap[row][column]], (column*tilesize,row*tilesize))
            
            
            
            
    screen.blit(background,(0,0))
    pygame.display.flip()       