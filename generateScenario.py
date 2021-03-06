import initial
import classes
import random
import graphics
import numpy as np
def start(energy):
    out=[]
    total=np.zeros((100,100))
    for i in range(10):
        out.append((random.randrange(100),random.randrange(100)))
    for point in out:
        total[point[0]][point[1]]=energy
    for i in range(3):
        total=total+initial.diffusion(.9,total,1)
        #print(total)
    return total

def setup(energies):
    
    listy=[start(element) for element in energies]
    return tuple(listy)

#hello=setup()

#graphics.drawEnergy(hello[0],hello[1],hello[2])
