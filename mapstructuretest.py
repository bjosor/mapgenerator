import random

class tiledata(object):
    def __init__(self):
        self = {"tile":random.randint(1,10),"walkable":random.randint(1,10)}

array = [[0 for a in range(10)]for b in range(10)]

print (array)

for a in range(10):
    for b in range(10):
        array[a][b] = tiledata()
    
