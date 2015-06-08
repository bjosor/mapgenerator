import pygame, sys, math, random

##-----------CLASSES--------------------
        


##-----------FUNCTIONS------------------



pygame.init()

BLUE = 0
RED  = 1

tiletextures = {
                BLUE  : pygame.image.load("blue_dot.png"),
                RED   : pygame.image.load("red_dot.png")
                }

tilesize = 32
mapwidth = 60
mapheight = 33

tiles = [BLUE,RED]
tilemap = [[BLUE for w in range(mapwidth)] for h in range(mapheight)]

screen = pygame.display.set_mode((tilesize*mapwidth,tilesize*mapheight),pygame.FULLSCREEN)
clock = pygame.time.Clock()

for rw in range(mapheight):
    for cl in range(mapwidth):
        randnum = random.randint(0,10)
        if randnum <= 3:
            tile = RED
        else:
            tile = BLUE
        tilemap[rw][cl] = tile

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
                
    for row in range(mapheight):
        for column in range (mapwidth):
            screen.blit(tiletextures[tilemap[row][column]], (column*tilesize,row*tilesize))
            
    pygame.display.flip()       