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

def metabolism(energies,organism,dt):
    return -energies*organism.metrate*dt
    

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
    return signal.convolve2d(diffused,kernel,boundary='wrap',mode='same')
    

eosprey[0][0]=90

for time in range(20):
    temp=diffusion(osprey,eosprey,dt)
    eosprey=temp
    print(temp[0][0])
print(osprey.predation)
efficiency = .5
epredators = np.array([eosprey])
for i in range(5):
	efish, epredators = consume.consume(efish, epredators, np.array([[osprey.predation, osprey.maxdist, efficiency]]), grid, .1)
#print(efish)
#print(eosprey)

#below function is under heavy development, should change substantially
def iter_model(organisms, energies, pollutions, plant_ambient, dt, grid, efficiency):
	x, plantAdd = consume.consume(np.full((grid,grid), plant_ambient), np.array([energies[0]]), np.array([[plant.predation, plant.maxdist, efficiency]]), grid, dt)
	
	plantRem, fishAdd = consume.consume(energies[0], np.array([energies[1]]), np.array([[fish.predation, fish.maxdist, efficiency]]), grid, dt)

	fishRem, ospreyAdd = consume.consume(energies[1], np.array([energies[2]]), np.array([[osprey.predation, ospprey.maxdist, efficiency]]), grid, dt)

	diffusDeltas = np.array([])
	for i in range(len(organisms)):
		diffDeltas.append(diffusion(organisms[i], energies[i], dt))
	
	metDeltas = np.array([])
	for i in range(len(organisms)):
		metDeltas.append(metabolism(energies[i], organisms[i], dt))
	
	
	
	
	energies[0] = energies[0] + plantAdd[0] + plantRem + diffusDeltas[0] + metDeltas[0]
	energies[1] = energies[1] + fishAdd[0] + fishRem + diffusDeltas[1] + metDeltas[1]
	energies[2] = energies[2] + ospreyAdd[0] + diffusDeltas[2] + metDeltas[2]

	#TODO POLLUTION
	return energies#, pollutions



	

