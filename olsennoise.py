#Copyright Tatarize 2014
#MIT License.
import math,pygame

def paint(seedx,seedy,width,height,iterations):
    onmap = fieldOlsenNoise(seedx, seedy, seedx+width, seedy+height, iterations)
    onmap = arrayblur(onmap)
    surface = pygame.Surface((width,height))
    for j in range(len(onmap)):
        for k in range(len(onmap[1])):
            color = onmap[j][k]
            print(color)
            surface.set_at((j,k),(color,color,color))
    return surface

def arrayblur(array):
    for a in range(len(array)):
        for b in range(len(array[0])):
            array[a][b] = array[a-1][b] + array[a][b-1] + array[a+1][b] + array[a][b+1] + array[a][b] + array[a][b]
            array[a][b] = array[a][b]/6
    return array
    


def fieldOlsenNoise(x0, y0, x1, y1, iterations):
    
    #OLSEN NOISE
    #assert x1 < x0 
        
    #assert y1 < y0
    
    finalwidth = x1 - x0
    finalheight = y1 - y0

    finalmap = createArray(finalwidth, finalheight)

    if iterations == 0:
        for j in range(finalwidth):
            for k in range(finalheight):
                rand = hashrandom(iterations, x0 + j, y0 + k) & (1 << (7 - iterations)) #add noise to map.
                finalmap[j][k] += rand
        return finalmap
    #base case of recursive call is simply random field of 128 and 0.


    ux0 = math.floor(x0 / 2) - 1
    uy0 = math.floor(y0 / 2) - 1
    ux1 = math.ceil(x1 / 2) + 1
    uy1 = math.ceil(y1 / 2) + 1
    #Calculate the size of the image needed to make the size of the image requested.

    uppermap = fieldOlsenNoise(ux0, uy0, ux1, uy1, iterations - 1)
    #Requests the field of the required size to make the current requested field.
    
    
    uw = ux1 - ux0
    uh = uy1 - uy0
    #current uppermap width and height.


    cx0 = ux0 * 2
    cy0 = uy0 * 2
    cw = uw * 2
    ch = uh * 2
    #scale all the current x,y,w,h to 2x current size for the upsampling.

    upsampledmap = createArray(cw, ch)
    
    for j in range(cw):
        for k in range(ch):
            rand = (hashrandom(iterations, cx0 + j, cy0 + k) & (1 << (7 - iterations))) #add noise to map.
            upsampledmap[j][k] = uppermap[math.floor(j / 2)][math.floor(k / 2)] + rand
    #upsampled and random noise addition.

    
        
    xoff = x0 - cx0;
    yoff = y0 - cy0;
    #Algorithm must track the position between different requests. x0 is the required value, and cxy is the position of the upper right value in the blurmap.
    
    
    #3x3 box blur will lose two points around edges.
    
    ch-=2
    for j in range(cw):
        for k in range(ch):
            upsampledmap[j][k] += upsampledmap[j][k+1] + upsampledmap[j][k+2]
    #blur 1x3
    
    cw-=2
    for k in range(ch):
        for j in range(cw):
            upsampledmap[j][k] += upsampledmap[j+1][k] + upsampledmap[j+2][k]
    #blur 1x3

    
    for j in range(finalwidth):
        for k in range(finalheight):
            finalmap[j][k] =  math.floor(upsampledmap[j + xoff][k + yoff] / 9)
        
    #trimmed and positioned.

    return finalmap #map of correct size is returned.

def singlehash(hash):
    rem = hash & 3
    h = hash

    if rem == 3:
        hash += h;
        hash ^= hash << 32
        hash ^= h << 36
        hash += hash >> 22
    elif rem == 2:
        hash += h
        hash ^= hash << 22
        hash += hash >> 34
    elif rem == 1:
            hash += h
            hash ^= hash << 20
            hash += hash >> 2

    hash ^= hash << 6
    hash += hash >> 10
    hash ^= hash << 8
    hash += hash >> 34
    hash ^= hash << 50
    hash += hash >> 12
    return hash & 0xFFFF
    #provides a hash of a given value.

def hashrandom(x,y,z): 
        hash = singlehash(x)
        hash = singlehash(hash ^ y)
        hash = singlehash(hash ^ z)
        return hash
        #Provides a hashed random value of any number of arguments.
    
def createArray(finalwidth,finalheight):
    print(finalwidth,finalheight)
    array = [[0 for a in range(finalwidth)]for b in range(finalheight)]
        
    return array
    #creates a zeroed array of given set values.

