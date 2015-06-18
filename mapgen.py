import pygame, sys, math, random, Diamondsquaregen

##-----------CLASSES--------------------
        
class spritesheet(object):
    # class to read/handle spritesheets, use images_at or load_strip
    # to load several images from a sheet
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error:
            print ('Unable to load spritesheet image:')
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

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
            if colormap[i][j] <= 125:
                tile = 0
            elif colormap[i][j] <= 255:
                tile = 1
        
            colormap[i][j] = tile
            
            
    return colormap


def check_neighbor(array,x,y,tile):
    # Creates a unique value for a tile depending on its neighbours
    binary = 0
    if array[x][y] == tile:
        neighbors = [array[x][y+1],array[x+1][y+1],array[x+1][y],array[x+1][y-1],array[x][y-1],array[x-1][y-1],array[x-1][y],array[x-1][y+1]]
        for index, a in enumerate(neighbors):
            if a == 1:
                if index == 0:
                    binary += 1
                elif index == 1:
                    binary += 2
                elif index == 2:
                    binary += 4
                elif index == 3:
                    binary += 8
                elif index == 4:
                    binary += 16
                elif index == 5:
                    binary += 32
                elif index == 6:
                    binary += 64
                elif index == 7:
                    binary += 128
                
                print(binary)
    return binary


def generate_map(randseed,mapsize):   
    image = Diamondsquaregen.paint(randseed,randseed,mapsize[0],mapsize[1],5).convert()
    
    tilesize = 64
    mapwidth = image.get_width()
    mapheight = image.get_height()
    
    WATER = "water"
    GRASS = "water"
    water = spritesheet("graphics/water.png")
    grass = spritesheet("graphics/grass.png")
    tiletextures = [water.load_strip((0,0,64,64),18,(255,255,255)),grass.load_strip((0,0,64,64),18,(255,255,255))]    
    
    tiles = [WATER,GRASS]
    tilemap = readhm(image)

    worldmap = pygame.Surface((mapwidth*tilesize,mapwidth*tilesize)) 
    
    #loop through all tiles except bordertiles
    for row in range(mapwidth)[1:-1]:
        for column in range (mapheight)[1:-1]:
            bitval = check_neighbor(tilemap,row,column,WATER)
            worldmap.blit(tiletextures[tilemap[row][column]][0], (column*tilesize,row*tilesize))
            #print (bitval)
            if bitval != 0:
                print ("kake")
                #worldmap.blit(tiletextures[tilemap[column][row]][bitval],(column*tilesize,row*tilesize))
                #worldmap.blit(sand,(column*tilesize,row*tilesize))
                
    return worldmap
            

#-----------MAIN BLOCK--------------

"""pygame.init()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

WATER = 0
GRASS = 1
water = spritesheet("graphics/water.png")
grass = spritesheet("graphics/grass.png")
bob = random.randint(1,1000000)
print(bob)

image = Diamondsquaregen.paint(bob,bob,128,128,5).convert()

tiletextures = [water.load_strip((0,0,64,64),18,(255,255,255)),grass.load_strip((0,0,64,64),18,(255,255,255))]


tilesize = 64
mapwidth = image.get_width()
mapheight = image.get_height()

sand = pygame.image.load("graphics/sand.png")

#--scrolling configuration----
scrollstepx = 15
scrollstepy = 15
cornerpoint = [0,0]

tiles = [WATER,GRASS]
tilemap = readhm(image)

#----surfaces and clock-----
clock = pygame.time.Clock()
worldmap = pygame.Surface((mapwidth*tilesize,mapwidth*tilesize))
mapdim = worldmap.get_size()
screensize = screen.get_size()
background = pygame.Surface(screen.get_size())
backgroundrect = background.get_rect()
background = worldmap.subsurface((cornerpoint[0],cornerpoint[1],mapdim[0],mapdim[1]))


#loop through all tiles except bordertiles
for row in range(mapwidth)[1:-1]:
        for column in range (mapheight)[1:-1]:
            bitval = check_neighbor(tilemap,row,column,WATER)
            worldmap.blit(tiletextures[tilemap[row][column]][0], (column*tilesize,row*tilesize))
            #print (bitval)
            if bitval != 0:
                print ("kake")
                #worldmap.blit(tiletextures[tilemap[column][row]][bitval],(column*tilesize,row*tilesize))
                #worldmap.blit(sand,(column*tilesize,row*tilesize))
                
            
worldmap.convert()





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
    """       