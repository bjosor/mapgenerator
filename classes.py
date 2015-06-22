import pygame, math, sys, random

class Ball(pygame.sprite.Sprite):
    selected = []
    img = [pygame.image.load('graphics/blue_dot.png'),pygame.image.load('graphics/blue_dot_sel.png'),
           pygame.image.load('graphics/red_dot.png')]

    ## Contains the base information of the instance
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = Ball.img[0]
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        Unitorg.units.append(self)
        self.target = None
        self.pos = (self.rect[0],self.rect[1])

    ##used each frame to update the state of the instance
    def update(self,seconds):

        #if a target has been set, move towards it and stop when reached
        if  self.target != None:
            speed=3
            dx = self.rect.x - self.target[0]
            dy = self.rect.y - self.target[1]
            dz = math.sqrt(dx**2 + dy**2)
            #print (dz)
            self.rect.x += (dx/dz*speed)*seconds
            self.rect.y += (dy/dz*speed)*seconds
                
            if self.rect[0] == self.target[0] and self.rect[1] == self.target[1]:
                self.target = None
            

            

    ## marks a unit as selected if clicked on, and deselects it if you click elsewhere
    def selection(self):
        if self.rect.collidepoint((pygame.mouse.get_pos())):
            if not self in Ball.selected:
                Ball.selected.append(self)
                self.image = Ball.img[1]
                print(Ball.selected)
            

        elif not self.rect.collidepoint((pygame.mouse.get_pos())):
            if self in Ball.selected:
                Ball.selected.remove(self)
                self.image = Ball.img[0]
                print(Ball.selected)





class config(object):
    screensize = (800,600)
    mapsize = (128,128)
    tilesize = 64
    fps = 30
    scrollstepx = 1
    scrollstepy = 1
    cornerpoint = [0,0]
    zoomspeed = 0.01
    zoom = 1.0

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

class tiledata(object):
    def __init__(self,data):
        self.data = data

class Town(object):
    stuff = "placeholder"  

##Class to keep track of units created
class Unitorg(object):

    units = []
    
  
    

