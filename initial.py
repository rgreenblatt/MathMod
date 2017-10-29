import random
import numpy as np

dt=1
tfin=10
grid=100

class Organism():
    predations=(0.9,0.5,0.4)
    diffusions=(0.05,0.2,0.15)
    metabolics=(0.2,0.3,0.4)
    distances=(0,10,50)
    names=("Plant","Fish","Osprey")
    def __init__(self,level):
        self.level=level
        self.predation=self.predations[level]
        self.diffusion=self.diffusions[level]
        self.metrate=self.metabolics[level]
        self.maxdist=self.distances[level]
    def __str__(self):
        return self.names[self.level]
    def __repr__(self):
        return str(self)
plant=Organism(0)
fish=Organism(1)
osprey=Organism(2)

eplant=np.full((grid,grid),1.0)
efish=np.full((grid,grid),1.0)
eosprey=np.full((grid,grid),1.0)


def metabolism(energies,organism,dt,grid):
    for i in range(grid):
        for k in range(grid):
            energies[i][k]-=energies[i][k]*organism.metrate*dt

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

def diffusion(organism,energies,dt,grid):
    diffused = np.multiply(energies,organism.diffusion*dt/8.0)
    energies = np.subtract(energies,diffused*8.0)
    energies = np.add(energies,np.roll(diffused,1,axis=0))
    energies = np.add(energies,np.roll(diffused,-1,axis=0))
    energies = np.add(energies,np.roll(diffused,1,axis=1))
    energies = np.add(energies,np.roll(diffused,-1,axis=1))
    
    energies = np.add(energies,np.roll(diffused,(1,1),axis=(0,1)))
    energies = np.add(energies,np.roll(diffused,(1,-1),axis=(0,1)))
    energies = np.add(energies,np.roll(diffused,(-1,1),axis=(0,1)))
    energies = np.add(energies,np.roll(diffused,(-1,-1),axis=(0,1)))
    return energies

eosprey[0][0]=90

for time in range(1000):
    temp=diffusion(osprey,eosprey,dt,grid)
    eosprey=temp
    print(temp[0][0])
