import pygame, random, math

pygame.init()


def diamondsquaredmap(x,y,width,height,iterations):
    dsmap = fieldDiamondSquared(x, y, x+width, y+height, iterations)
    maxdeviation = getMaxDeviation(iterations)
     
    for j in range(width):
        for k in range(height): 
            dsmap[j][k] = dsmap[j][k] / maxdeviation
            dsmap[j][k] = (dsmap[j][k] + 1) / 2
            
    return dsmap

def create2DArray(d1, d2):
        x = [[0 for i in range(d1)] for j in range(d2)]  
        return x

def fieldDiamondSquared(x0, y0, x1, y1, iterations):
        assert (x1 > x0)
        assert (y1 > y0)
        finalwidth  = x1 - x0
        finalheight = y1 - y0
        finalmap = create2DArray(finalwidth, finalheight)
        if iterations == 0:
            for j in range(finalwidth):
                for k in range(finalheight):
                    finalmap[j][k] =  displace(iterations,x0+j,y0+k) 

            return finalmap;
        
        ux0 = math.floor(x0 / 2) - 1
        uy0 = math.floor(y0 / 2) - 1
        ux1 = math.ceil(x1 / 2) + 1
        uy1 = math.ceil(y1 / 2) + 1
        uppermap = fieldDiamondSquared(ux0, uy0, ux1, uy1, iterations-1)

        uw = ux1 - ux0
        uh = uy1 - uy0
        
        cx0 = ux0 * 2
        cy0 = uy0 * 2

        cw = uw*2-1
        ch = uh*2-1
        currentmap = create2DArray(cw,ch)
        

        for j in range(uw):
            for k in range(uh):
                currentmap[j*2][k*2] = uppermap[j][k]
                
        xoff = x0 - cx0
        yoff = y0 - cy0
        for j in range(cw)[1:-1:2]:
            for k in range(cw)[1:-1:2]:
                currentmap[j][k] = ((currentmap[j-1][k-1] + currentmap[j-1][k+1] + currentmap[j+1][k-1] + currentmap[j+1][k+1]) / 4) + displace(iterations,cx0+j,cy0+k)
        
        for j in range(cw)[1:-1:2]:
            for k in range(ch)[2:-1:2]:
                currentmap[j][k] = ((currentmap[j - 1][k] + currentmap[j + 1][k] + currentmap[j][k - 1] + currentmap[j][k + 1]) / 4) + displace(iterations,cx0+j,cy0+k)
                
        for j in range(cw)[2:-1:2]:
            for k in range(ch)[1:-1:2]:
                currentmap[j][k] = ((currentmap[j - 1][k] + currentmap[j + 1][k] + currentmap[j][k - 1] + currentmap[j][k + 1]) / 4) + displace(iterations,cx0+j,cy0+k)
            
        

        for j in range(finalwidth):
            for k in range(finalheight):
                finalmap[j][k] = currentmap[j+xoff][k+yoff]
            
        
        
        return finalmap
    

    # Random function to offset
def displace(iterations, x, y):
    return (((PRH(iterations,x,y) - 0.5)*2)) / (iterations+1)
    
    
def getMaxDeviation(iterations):
    dev = 0.5 / (iterations+1)
    if iterations <= 0: 
        return dev
    return getMaxDeviation(iterations-1) + dev

    #This function returns the same result for given values but should be somewhat random.
def PRH(iterations,x,y):
    #print("hashing stuff")
    x = x & 0xFFF
    y = y & 0xFFF
    iterations & 0xFF
    hash = (iterations << 24)
    hash = hash|(y << 12)
    hash = hash| x
    rem = hash & 3
    h = hash
    print(rem)

    if rem == 3:
        hash += h
        hash = hash ^ hash << 32
        hash = hash ^ h << 36
        hash += hash >> 22
        print("hash 3")
                
    elif rem == 2:
        hash += h
        hash = hash ^ hash << 22
        hash += hash >> 34
        print("hash 2")
                
    elif rem == 1:
        hash += h
        hash ^= hash << 20
        hash += hash >> 2
        print("hash 1")
                
    hash = hash ^ hash << 6
    hash += hash >> 10
    hash = hash ^ hash << 8
    hash += hash >> 34
    hash = hash ^ hash << 50
    hash += hash >> 12
        
    return (hash & 0xFFFF) / 0xFFFF

def paint(seedx,seedy,width,height,iterations):
    dsmap = diamondsquaredmap(seedx, seedy, width, height, iterations)
    surface = pygame.Surface((width,height))
    for j in range(len(dsmap)):
        for k in range(len(dsmap[1])):
            color = abs(math.floor(dsmap[j][k]*250))
            if color > 255:
                color = 255
            #print(color)

            surface.set_at((j,k),(color,color,color))
    return surface

#screen = pygame.display.set_mode((512,512))
#background = paint(512,512,5)
             
#while True:
#    screen.blit(background,(0,0))
#    pygame.display.flip()




