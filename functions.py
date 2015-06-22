import pygame
from classes import *

def scroll():
    scrollx = 0
    scrolly = 0
    pressedkeys = pygame.key.get_pressed()
                 
    # --- handle keys to scroll map ----
    if pressedkeys[pygame.K_LEFT]:
        scrollx += config.scrollstepx
    if pressedkeys[pygame.K_RIGHT]:
        scrollx -= config.scrollstepx
    if pressedkeys[pygame.K_UP]:
        scrolly += config.scrollstepy
    if pressedkeys[pygame.K_DOWN]:
        scrolly -= config.scrollstepy
    # -------- scroll the visible part of the map ------
    config.cornerpoint[0] += scrollx
    config.cornerpoint[1] += scrolly
    

def drawmap(mapdata):
    water = spritesheet("graphics/water.png")
    grass = spritesheet("graphics/grass.png")
    tiletextures = [water.load_strip((0,0,64,64),18,(255,255,255)),grass.load_strip((0,0,64,64),18,(255,255,255))]
    scroll()
    background = pygame.Surface((50*64,30*64))
    for a in range(int(config.cornerpoint[0]),int(config.cornerpoint[0]) + 100):
        for b in range(int(config.cornerpoint[1]),int(config.cornerpoint[1]) + 60):
            if mapdata[a][b]["tileval"] == 0:
                #print("water")
                background.blit(tiletextures[0][0],(config.cornerpoint[0]+(a*64),config.cornerpoint[1]+(b*64)))
            elif mapdata[a][b]["tileval"] == 1:
                #print("grass")
                background.blit(tiletextures[1][0],(config.cornerpoint[0]+(a*64),config.cornerpoint[1]+(b*64)))
                
    screen = background.subsurface((128,128,config.screensize[0],config.screensize[1]))
            
    return screen

    """if config.cornerpoint[0] < 0:
            config.cornerpoint[0] = 0
            scrollx = 0
    elif config.cornerpoint[0] > mapdim[0] - config.screensize[0]:
            config.cornerpoint[0] = mapdim[0] - config.screensize[0]
            scrollx = 0
    if config.cornerpoint[1] < 0:
            config.cornerpoint[1] = 0
            scrolly = 0
    elif config.cornerpoint[1] > mapdim[1] - config.screensize[1]:
            config.cornerpoint[1] = mapdim[1] - config.screensize[1]
            scrolly = 0

    #if scrollx == 0 and scrolly == 0:    # only necessary if there was no scrolling
        #sprites.clear(screen, background)

    else:
        background = themap.subsurface((config.cornerpoint[0],
                                            config.cornerpoint[1],
                                            config.screensize[0],
                                            config.screensize[1])) # take snapshot of bigmap"""