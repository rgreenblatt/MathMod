import initial
import classes
import random
import graphics
import numpy as np
def start(organism):
    out=[]
    total=np.zeros((100,100))
    for i in range(10):
        out.append((random.randrange(100),random.randrange(100)))
    for point in out:
        total[point[0]][point[1]]=100
    for i in range(30):
        total=initial.diffusion(organism,total,initial.dt)
    return total

def setup():
    orgs=[classes.Organism(k) for k in range(3)]
    listy=[start(i) for i in orgs]
    return tuple(listy)

print(setup())