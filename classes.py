import pygame, math, sys, random


class config(object):
    width = 800
    height = 600
    xtiles = 15
    ytiles = 15
    fps = 30
    scrollstepx = 15
    scrollstepy = 15
    cornerpoint = [0,0]
    zoomspeed = 0.01
    zoom = 1.0


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


##Class to keep track of units created
class Unitorg(object):

    units = []
    
class Town(object):
    stuff = "placeholder"    
    

