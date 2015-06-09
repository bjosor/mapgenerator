import pygame, sys, math, random

##-----------CLASSES--------------------
        


##-----------FUNCTIONS------------------
    
def readhm(image):
    # converts a grayscale heightmap into a tilemap
    imgwidth = image.get_width()
    imgheight = image.get_height()
    colormap = [[0 for r in range(imgheight)] for cl in range(imgwidth)]
    
    # store color per pixel of heightmap in 2d array
    for x in range(imgwidth):
        for y in range(imgheight):
            color = image.get_at((x,y))
            colormap[x][y] = color[0]

    # exchange color value for corresponding tile ID
    for i in range(imgwidth):
        for j in range(imgheight):
            if colormap[i][j] <= 5:
                tile = WATER
            elif colormap[i][j] <= 30:
                    tile = SAND
            elif colormap[i][j] <= 100:
                tile = GRASS
            elif colormap[i][j] <= 150:
                tile = MOSS
            else:
                tile = ROCK
        
            colormap[i][j] = tile
    
    for x in range(1,imgwidth-1):
        print(x)
        for y in range(1,imgheight-1):
            print(y)
            relations = check_neighbour(colormap,x,y)
            if colormap[x][y] == SAND and relations.count(GRASS) == 2:
                    colormap[x][y] = SANDGRASS
            
    return colormap


def check_neighbour(array,x,y):
    neighbours = [array[x+1][y],array[x][y+1],array[x-1][y],array[x][y-1]]
    return neighbours


#-----------MAIN BLOCK--------------

pygame.init()

WATER = 0
SAND  = 1
GRASS = 3
MOSS  = 4
ROCK  = 5
SANDGRASS = 6

image = pygame.image.load("erosion.jpg")

tiletextures = {
                WATER  : pygame.image.load("water.png"),
                SAND   : pygame.image.load("sand32px.png"),
                GRASS  : pygame.image.load("grass32px.png"),
                MOSS   : pygame.image.load("heightgrass.png"),
                ROCK   : pygame.image.load("rock.png"),
                SANDGRASS:pygame.image.load("grass_sand.png")
                }

tilesize = 32
mapwidth = image.get_width()
mapheight = image.get_height()

#--scrolling configuration----
scrollstepx = 15
scrollstepy = 15
cornerpoint = [0,0]

tiles = [WATER,SAND,GRASS,MOSS,ROCK,SANDGRASS]
tilemap = readhm(image)

#----surfaces and clock-----
clock = pygame.time.Clock()
worldmap = pygame.Surface((mapwidth*tilesize,mapwidth*tilesize))
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
mapdim = worldmap.get_size()
screensize = screen.get_size()
background = pygame.Surface(screen.get_size())
backgroundrect = background.get_rect()
background = worldmap.subsurface((cornerpoint[0],cornerpoint[1],mapdim[0],mapdim[1]))

for row in range(mapwidth):
        for column in range (mapheight):
            worldmap.blit(tiletextures[tilemap[column][row]], (column*tilesize,row*tilesize))





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
                
    
                
    scrollx = 0
    scrolly = 0
    pressedkeys = pygame.key.get_pressed()
                 
    # --- handle keys to scroll map ----
    if pressedkeys[pygame.K_LEFT]:
        scrollx -= scrollstepx
    if pressedkeys[pygame.K_RIGHT]:
        scrollx += scrollstepx
    if pressedkeys[pygame.K_UP]:
        scrolly -= scrollstepy
    if pressedkeys[pygame.K_DOWN]:
        scrolly += scrollstepy
    # -------- scroll the visible part of the map ------
    cornerpoint[0] += scrollx
    cornerpoint[1] += scrolly

    if cornerpoint[0] < 0:
            cornerpoint[0] = 0
            scrollx = 0
    elif cornerpoint[0] > mapdim[0] - screensize[0]:
            cornerpoint[0] = mapdim[0] - screensize[0]
            scrollx = 0
    if cornerpoint[1] < 0:
            cornerpoint[1] = 0
            scrolly = 0
    elif cornerpoint[1] > mapdim[1] - screensize[1]:
            cornerpoint[1] = mapdim[1] - screensize[1]
            scrolly = 0


    else:
        background = worldmap.subsurface((cornerpoint[0],
                                            cornerpoint[1],
                                            screensize[0],
                                            screensize[1])) # take snapshot of bigmap
                
    
            
            
            
            
    screen.blit(background,(0,0))
    pygame.display.flip()       