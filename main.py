import pygame, math, sys, random, mapgen
from classes import *
from functions import *


# Initialise screen
pygame.init()
screen = pygame.display.set_mode((config.screensize[0], config.screensize[1]))

#-----------------Get maparray, load gfx and prepare surfaces ---------------------
themap = mapgen.generate_map(678901,(128,128))

water = spritesheet("graphics/water.png")
grass = spritesheet("graphics/grass.png")
tiletextures = [water.load_strip((0,0,64,64),18,(255,255,255)),grass.load_strip((0,0,64,64),18,(255,255,255))] 


clock = pygame.time.Clock()

background = pygame.Surface((50*64,30*64)).convert()





mainloop = True
while mainloop:
    milliseconds = clock.tick(30)
    seconds = milliseconds/1000.0
    pygame.display.set_caption('fps:%f'%clock.get_fps())

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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in Unitorg.units:
                i.selection()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for i in Ball.selected:
                i.target = pygame.mouse.get_pos()
                


    # -----------SCROLLING------------------------
        



    #updates units
    
    background = drawmap(themap)
    #updates the screen
    screen.blit(background,(0,0))
    #sprites.clear(screen, background)
    pygame.display.flip()



