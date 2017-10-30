import random
import numpy as np
import classes
import consumeFunc as consume
from scipy import signal

dt=1
tfin=10
grid=100

plant=classes.Organism(0)
fish=classes.Organism(1)
osprey=classes.Organism(2)

eplant=np.full((grid,grid),1.0)
efish=np.full((grid,grid),1.0)
eosprey=np.full((grid,grid),1.0)

pplant=np.full((grid,grid),0.0)
pfish=np.full((grid,grid),1.0)
posprey=np.full((grid,grid),1.0)

def metabolism(energies,organism,dt,grid):
    for i in range(grid):
        for k in range(grid):
            energies[i][k]-=energies[i][k]*organism.metrate*dt

'''
def neighfind(i,k,grid):
    if k==grid-1 and i==grid-1:
        neighbors=[(i-1,k),(i-1,k-1),(i,k-1)]
    elif k==grid-1 and i==0:
        neighbors=[(i+1,k),(i,k-1),(i+1,k-1)]
    elif k==0 and i==grid-1:
        neighbors=[(i,k+1),(i-1,k),(i-1,k+1)]
    elif k==0 and i==0:
        neighbors=[(i+1,k),(i,k+1),(i+1,k+1)]
    elif i==grid-1:
        neighbors=[(i-1,k),(i-1,k+1),(i,k-1),(i,k+1),(i-1,k-1)]
    elif k==grid-1:
        neighbors=[(i-1,k),(i+1,k),(i,k-1),(i+1,k-1),(i-1,k-1)]
    elif k==0:
        neighbors=[(i,k+1),(i-1,k),(i+1,k),(i-1,k+1),(i+1,k+1)]
    elif i==0:
        neighbors=[(i,k+1),(i+1,k),(i,k-1),(i+1,k+1),(i+1,k-1)]
    else:
        neighbors=[(i-1,k),(i+1,k),(i,k+1),(i,k-1),(i+1,k+1),(i-1,k+1),(i+1,k-1),(i-1,k-1)]
    return neighbors
'''

def diffusion(organism,energies,dt):
    kernel = [[1,1,1],[1,-8,1],[1,1,1]]
    diffused = np.multiply(energies,organism.diffusion*dt/8.)
    energies = energies + signal.convolve2d(diffused,kernel,boundary='wrap',mode='same')
    return energies

eosprey[0][0]=90

for time in range(20):
    temp=diffusion(osprey,eosprey,dt)
    eosprey=temp
    print(temp[0][0])
print(osprey.predation)
effeciency = .5
epredators = np.array([eosprey])
for i in range(5):
	efish, epredators = consume.consume(efish, epredators, np.array([[osprey.predation, osprey.maxdist, effeciency]]), grid, .1)
#print(efish)
#print(eosprey)

