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
        
            colormap[i][j] = {"tileval":tile}
            
            
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


def generate_map(seed,mapsize):   
    image = Diamondsquaregen.paint(seed,seed,mapsize[0],mapsize[1],5).convert()
    
    tilemap = readhm(image)
    
    return tilemap

    

