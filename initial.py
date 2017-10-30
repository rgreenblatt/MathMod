import random
import numpy as np
import classes
import consumeFunc as consume
import graphics
from scipy import signal
import circleGener as circ

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
pfish=np.full((grid,grid),0.0)
posprey=np.full((grid,grid),0.0)

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

#def pollutionKill(organism, energies, pollutions, dt):
	
def diffusion(organism,energies,dt):
    #kernel = [[1,1,1],[1,-8,1],[1,1,1]]
    kernel = circ.gener(8)
    diffused = 0.9*energies*dt
    norm_diffused = diffused/np.sum(kernel)
    convolve = signal.convolve2d(norm_diffused,kernel,boundary='wrap',mode='same')-diffused
    return convolve
    

eosprey[0][0]=90

for time in range(10):
	temp=eosprey+diffusion(osprey,eosprey,dt)
	eosprey=temp
	print(temp[0][0])
	graphics.drawEnergy(temp, np.zeros(temp.shape), np.zeros(temp.shape))
#print(osprey.predation)
#efficiency = .5
#epredators = np.array([eosprey])
#for i in range(5):
#	efish, epredators = consume.consume(efish, epredators, np.array([[osprey.predation, osprey.maxdist, efficiency]]), grid, .1)
#print(efish)
#print(eosprey)
def reformatPandE(energy, pollution):
	return np.swapaxes(np.array([energy, pollution]), 2, 0)


#below function is under heavy development, should change substantially
	
def iter_model(organisms, energies, pollutions, plant_ambient, dt, grid, efficiency, pTransfer):
	epambient = reformatPandE(np.full((grid,grid), plant_ambient), np.zeros((grid, grid)))
		
	epplant = reformatPandE(energies[0], pollutions[0])


	x, y, plantAdd, z = consume.consume(epambient, np.array([epplant]), np.array([[plant.predation, plant.maxdist, efficiency, 0]]), grid, dt)
	
	
	

	plantRemE, plantRemP, fishAddE, fishAddP = consume.consume(reformatPandE(energies[0], pollutions[0]), np.array([reformatPandE(energies[1], pollutions[1])]), np.array([[fish.predation, fish.maxdist, efficiency, pTransfer]]), grid, dt)

	fishRemE, fishRemP, ospreyAddE, ospreyAddP = consume.consume(reformatPandE(energies[1], pollutions[1]), np.array([reformatPandE(energies[2], pollutions[2])]), np.array([[osprey.predation, osprey.maxdist, efficiency, pTransfer]]), grid, dt)

	diffusDeltas = []
	for i in range(len(organisms)):
		diffusDeltas.append(diffusion(organisms[i], energies[i], dt))
	
	metDeltas = []
	for i in range(len(organisms)):
		metDeltas.append(metabolism(energies[i], organisms[i], dt))
	
	
	
	#print(plantAdd[0])	
	energies[0] = energies[0] + plantAdd[0] + plantRemE + diffusDeltas[0] + metDeltas[0]
	energies[1] = energies[1] + fishAddE[0] + fishRemE + diffusDeltas[1] + metDeltas[1]
	energies[2] = energies[2] + ospreyAddE[0] + diffusDeltas[2] + metDeltas[2]

	pollutions[0] = pollutions[0] + plantRemP
	pollutions[1] = pollutions[1] + fishAddP[0] + fishRemP
	pollutions[2] = pollutions[2] + ospreyAddP[0]

	#TODO POLLUTION
	return energies, pollutions

energyByTimeP = []
energyByTimeH = []
energyByTimeC = []

#energies = np.array([eplant, efish, eosprey])
#pollutions = np.array([pplant, pfish, posprey])
#for i in range(100):
#	energyByTimeP.append(energies[0])
#	energyByTimeH.append(energies[1])
#	energyByTimeC.append(energies[2])
#	energies, pollutions = iter_model(np.array([plant, fish, osprey]), energies, pollutions, .2, 1, grid, .8, .6)
#	print(i)	
#graphics.animEnergy(np.array(energyByTimeP), np.array(energyByTimeH), np.array(energyByTimeC))
	

