import pygame, math, sys, random, classes, mapgen


class config(object):
    width = 1200
    height = 800
    xtiles = 15
    ytiles = 15
    fps = 30
    scrollstepx = 15
    scrollstepy = 15
    cornerpoint = [0,0]
    zoomspeed = 0.01
    zoom = 1.0


# Initialise screen
pygame.init()
screen = pygame.display.set_mode((config.width, config.height))
#-----------------Loads-Map-Image---------------------
themap = mapgen.generate_map(678901,(128,128))


mapdim = themap.get_size()
themap_origin = themap.copy()
background = pygame.Surface((screen.get_size()))
backgroundrect = background.get_rect()
background = themap.subsurface((classes.config.cornerpoint[0],classes.config.cornerpoint[1],
                                classes.config.width,classes.config.height))
background = background.convert()
backgroundcopy = background.copy()
screen.blit(background,(0,0))
clock = pygame.time.Clock()

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()




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
            for i in classes.Unitorg.units:
                i.selection()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for i in classes.Ball.selected:
                i.target = pygame.mouse.get_pos()
                


    # -----------SCROLLING------------------------
        
    scrollx = 0
    scrolly = 0
    pressedkeys = pygame.key.get_pressed()
                 
    # --- handle keys to scroll map ----
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

    if config.cornerpoint[0] < 0:
            config.cornerpoint[0] = 0
            scrollx = 0
    elif config.cornerpoint[0] > mapdim[0] - config.width:
            config.cornerpoint[0] = mapdim[0] - config.width
            scrollx = 0
    if config.cornerpoint[1] < 0:
            config.cornerpoint[1] = 0
            scrolly = 0
    elif config.cornerpoint[1] > mapdim[1] - config.height:
            config.cornerpoint[1] = mapdim[1] - config.height
            scrolly = 0

    #if scrollx == 0 and scrolly == 0:    # only necessary if there was no scrolling
        #sprites.clear(screen, background)

    else:
        background = themap.subsurface((config.cornerpoint[0],
                                            config.cornerpoint[1],
                                            config.width,
                                            config.height)) # take snapshot of bigmap


    #updates units
    

    #updates the screen
    screen.blit(background,(0,0))
    #sprites.clear(screen, background)
    pygame.display.flip()


##
####--------------------ZOOM-----------(WIP)--------------------------------
####
####
####    # zoom with o and l key
####    zoomfactor = 1.0 # neither o nor l, no zooming
####    
####    if pressedkeys[pygame.K_o]:
####        zoomfactor += config.zoomspeed
####    if pressedkeys[pygame.K_l]:
####        zoomfactor -= config.zoomspeed
####    if config.zoom >= 1.2:
####        config.zoom = 1.2
####
####    if zoomfactor !=1.0:
####        config.zoom *= zoomfactor
####        print (config.zoom)
####        themap = pygame.transform.rotozoom(themap_origin,0,config.zoom).convert()
##             
##
##    screen.blit(background, (0,0))
##
##    pygame.display.flip()

