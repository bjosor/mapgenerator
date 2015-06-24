import pygame, math


class commonfolk(pygame.sprite.Sprite):
    m_objectlist = []
    selected = []
    img = [pygame.image.load('graphics/villager01.png'),pygame.image.load('graphics/villager01_sel.png')]
    ## Contains the base information of the instance
    def __init__(self,pos,mobilegroup):
        #img = [pygame.image.load('graphics/villager01.png'),pygame.image.load('graphics/villager01_sel.png')]

        pygame.sprite.Sprite.__init__(self,mobilegroup)
        self.image = commonfolk.img[0]
        self.rect = self.image.get_rect()
        self.pos = pos
        self.truex = self.pos[0]
        self.truey = self.pos[1]
        self.rect.center = (self.truex,self.truey)
        Unitorg.units.append(self)
        self.target = None
        self.speed = 1


    ##used each frame to update the state of the instance
    def update(self,seconds):

        #if a target has been set, move towards it and stop when reached
        if  self.target != None:
            distance = [self.target[0] - self.truex, self.target[1] - self.truey]
            
            self.angle = math.atan2(distance[0],distance[1])
          
            self.truex += math.sin(self.angle) * self.speed
            self.truey -= math.cos(self.angle) * self.speed
            
            self.rect.center = (round(self.truex),round(self.truey))


            

    ## marks a unit as selected if clicked on, and deselects it if you click elsewhere
    def selection(self):
        if self.rect.collidepoint((pygame.mouse.get_pos())):
            if not self in commonfolk.selected:
                commonfolk.selected.append(self)
                self.image = commonfolk.img[1]
                print(commonfolk.selected)
            

        elif not self.rect.collidepoint((pygame.mouse.get_pos())):
            if self in commonfolk.selected:
                commonfolk.selected.remove(self)
                self.image = commonfolk.img[0]
                print(commonfolk.selected)
                
                
class S_object(pygame.sprite.Sprite):
    s_objectlist = []





class config(object):
    screensize = (1920,1080)
    mapsize = (512,512)
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
        return {a:self.image_at(rect, colorkey) for a,rect in enumerate(rects)}
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        tups = []
        for x in range(image_count):
            tups.append((rect[0]+rect[2]*x, rect[1], rect[2], rect[3]))
        for x in range(image_count):
            tups.append(((rect[0]+64)+rect[2]*x, rect[1], rect[2], rect[3]))
        "Loads a strip of images and returns them as a list"
        #tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
        #       for x in range(image_count)]
        return self.images_at(tups, colorkey)

class tiledata(object):
    def __init__(self,data):
        self.data = data

class farm(object):
    stuff = "placeholder"  

##Class to keep track of units created
class Unitorg(object):

    units = []
    
  
    

