import initial
import classes
import random
import graphics
import numpy as np
def setup(organism):
    out=[]
    total=np.zeros((100,100))
    for i in range(10):
        out.append((random.randrange(100),random.randrange(100)))
    for point in out:
        total[point[0]][point[1]]=100
    for i in range(30):
        total=initial.diffusion(organism,total,initial.dt)
    return total

hello=setup(classes.Organism(1))
graphics.drawEnergy(hello)
