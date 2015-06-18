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
            #print("last finalmap returned")            
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
            
        
        #print("finalmap returned")
        return finalmap
    

    # Random function to offset
def displace(iterations, x, y):
    return (((PRH(iterations,x,y) - 0.5)*2)) / (iterations+1)
    
    
def getMaxDeviation(iterations):
    dev = 0.5 / (iterations+1)
    if iterations <= 0: 
        return dev
    #print("maxdev gotten", (getMaxDeviation(iterations-1) + dev))
    return getMaxDeviation(iterations-1) + dev

    #This function returns the same result for given values but should be somewhat random.
def PRH(iterations,x,y):
    #print("hashhing stuff")
    x = x & 0xFFF
    y = y & 0xFFF
    iterations & 0xFF
    hashh = (iterations << 24)
    hashh = hashh|(y << 12)
    hashh = hashh| x
    rem = hashh & 3
    h = hashh

    if rem == 3:
        hashh += h
        hashh = hashh ^ hashh << 32
        hashh = hashh ^ h << 36
        hashh += hashh >> 22
                
    elif rem == 2:
        hashh += h
        hashh = hashh ^ hashh << 22
        hashh += hashh >> 34
                
    elif rem == 1:
        hashh += h
        hashh ^= hashh << 20
        hashh += hashh >> 2
                
    hashh = hashh ^ hashh << 6
    hashh += hashh >> 10
    hashh = hashh ^ hashh << 8
    hashh += hashh >> 34
    hashh = hashh ^ hashh << 50
    hashh += hashh >> 12
        
    #print((hashh & 0xFFFF) / 0xFFFF)
    return (hashh & 0xFFFF) / 0xFFFF

def paint(seedx,seedy,width,height,iterations):
    dsmap = diamondsquaredmap(seedx, seedy, width, height, iterations)
    surface = pygame.Surface((width,height))
    for j in range(len(dsmap)):
        for k in range(len(dsmap[1])):
            color = abs(math.floor(dsmap[j][k]*250))
            if color > 255:
                color = 255
            color -= 10
            if color < 0:
                color = 0
            #print(color)

            surface.set_at((j,k),(color,color,color))
    return surface

#screen = pygame.display.set_mode((512,512))
#background = paint(512,512,5)
             
#while True:
#    screen.blit(background,(0,0))
#    pygame.display.flip()




