import pygame, sys, math, random, Diamondsquaregen, olsennoise

##-----------CLASSES--------------------
        

##-----------FUNCTIONS------------------
    
def readhm(array):
    maxarray = map(max,array)
    minarray = map(min,array)
    a = min(minarray)
    b = max(maxarray)

    for x in range(len(array)):
        for y in range(len(array[0])):
            array[x][y] = 1 + (array[x][y]-a)*(100-1)/(b-a)


    # exchange value for corresponding tile ID
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] <= 50:
                tile = 0
            elif array[i][j] <= 75:
                tile = 1
            elif array[i][j] <= 100:
                tile = 2
                
            
            array[i][j] = tile
        
            
            
    return array


def check_neighbor(array,x,y,tile):
    # Creates a unique value for a tile depending on its neighbours
    binary = 0
    #print(x,y)
    if x >= 1 and x <= len(array)-2 and y >= 1 and y <= len(array[0])-2:
        if array[x][y]["tileval"] == 0:
            neighbors = [array[x-1][y]["tileval"],array[x][y-1]["tileval"],array[x+1][y]["tileval"],array[x][y+1]["tileval"]]
            for index, a in enumerate(neighbors):
                if a != tile:
                    #print("a and tile",a,tile)
                    if index == 0:
                        binary += 1
                    elif index == 1:
                        binary += 2
                    elif index == 2:
                        binary += 4
                    elif index == 3:
                        binary += 8               
    #print(binary)
    return binary

def generate_minimap(tilemap,mapsize):
    minimap = pygame.Surface(mapsize).convert()
    for a in range(mapsize[0]):
        for b in range(mapsize[1]):
            if tilemap[a][b] == 0:
                minimap.set_at((a,b),(96,104,202))
            if tilemap[a][b] == 1:
                minimap.set_at((a,b),(126,184,92))
            if tilemap[a][b] == 2:
                minimap.set_at((a,b),(150,150,150))
                
    #minimap = pygame.transform.scale(minimap, (300,300))
    
    return minimap
            


def generate_map(seed,mapsize):   
    image = Diamondsquaregen.paint(seed,seed,mapsize[0],mapsize[1],6)
    
    tilemap = readhm(image)
    minimap = generate_minimap(tilemap,mapsize)
    
    return tilemap,minimap

    

