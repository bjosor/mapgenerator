import pygame, math, sys, random, mapgen
from classes import *
from pygame.constants import FULLSCREEN

def update_minimap(minimap,copy):
    minimap.blit(copy,(0,0))
    screenpos = pygame.Rect(config.cornerpoint[0], config.cornerpoint[1], int(config.screensize[0]/64), int(config.screensize[1]/64))
    pygame.draw.rect(minimap,(255,255,255),screenpos,1)

def drawmap(tilearray,surface,focus):
    x = -1
    for a in range(focus[0],focus[0]+int(config.screensize[0]/64)+2):
        y = -1
        x += 1
        for b in range(focus[1],focus[1]+int(config.screensize[1]/64)+2):
            y += 1
            try:
                if tilearray[a][b]["tileval"] == 0:
                    surface.blit(tiletextures[0][0],(x*64,y*64))
                elif tilearray[a][b]["tileval"] == 1:
                    surface.blit(tiletextures[1][0],(x*64,y*64))
                elif tilearray[a][b]["tileval"] == 2:
                    surface.blit(tiletextures[2][0],(x*64,y*64))
            except:
                pass
                
    return surface
            
def scroll():
    scrollx = 0
    scrolly = 0
    pressedkeys = pygame.key.get_pressed()
    # --- handle Cursor keys to scroll map ----
    if pressedkeys[pygame.K_LEFT]:
        scrollx -= config.scrollstepx
    if pressedkeys[pygame.K_RIGHT]:
        scrollx += config.scrollstepx
    if pressedkeys[pygame.K_UP]:
        scrolly -= config.scrollstepy
    if pressedkeys[pygame.K_DOWN]:
        scrolly += config.scrollstepy
        # -------- scroll the visible part of the map ------
    config.cornerpoint[0] += scrollx
    config.cornerpoint[1] += scrolly
#--------- do not scroll out of bigmap edge -----
    if config.cornerpoint[0] < 0:
        config.cornerpoint[0] = 0
        scrollx = 0
    elif config.cornerpoint[0] > config.mapsize[0] - int(config.screensize[0]/64+1):
        config.cornerpoint[0] = config.mapsize[0] - int(config.screensize[0]/64+1)
        scrollx = 0
    if config.cornerpoint[1] < 0:
        config.cornerpoint[1] = 0
        scrolly = 0
    elif config.cornerpoint[1] > config.mapsize[1] - int(config.screensize[1]/64+2):
        config.cornerpoint[1] = config.mapsize[1] - int(config.screensize[1]/64+2)
        scrolly = 0    

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((config.screensize[0], config.screensize[1]), FULLSCREEN)

#-----------------Get maparray, load gfx and prepare surfaces ---------------------
themap,minimap = mapgen.generate_map(random.randint(1,100000),(config.mapsize[0],config.mapsize[1]))
minimapcopy=minimap.copy()

water = spritesheet("graphics/water.png")
grass = spritesheet("graphics/grass.png")
rock  = spritesheet("graphics/rock.png")  
tiletextures = [water.load_strip((0,0,64,64),18,(255,255,255)),grass.load_strip((0,0,64,64),18,(255,255,255)),rock.load_strip((0,0,64,64),18,(255,255,255))] 
terrain = pygame.Surface((config.screensize[0]+128,config.screensize[1]+128))

clock = pygame.time.Clock()

config.cornerpoint = [0,0]





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
    scroll()
    terrain = drawmap(themap,terrain,config.cornerpoint)
    update_minimap(minimap,minimapcopy)
    #updates the screen
    screen.blit(terrain,(-64,-64))
    screen.blit(minimap,(0,0))
    #sprites.clear(screen, background)
    pygame.display.flip()



