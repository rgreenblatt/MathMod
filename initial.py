import random
import sys
import numpy as np
import classes
import consumeFunc as consume
import graphics
from scipy import signal
import circleGener as circ
import pollutionFunc as pollute
import pollutant

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
	
def diffusion(diffus, energies, dt):
    #kernel = [[1,1,1],[1,-8,1],[1,1,1]]
    kernel = circ.gener(8)
    diffused = diffus*energies
    norm_diffused = diffused/np.sum(kernel)
    convolve = signal.convolve2d(norm_diffused,kernel,boundary='wrap',mode='same')-diffused
    return convolve
    



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
	
def iter_model(organisms, energies, pollutions, dt, grid, efficiency, pTransfer, ambientEnergy, ambient_pollution, absorbtionRate):
	
	epambient = reformatPandE(np.full((grid,grid), ambientEnergy), np.zeros((grid, grid)))
	producers = []

	for i in range(organisms.shape[0]):
		
		change = np.zeros((organisms.shape[0], 2, grid, grid))
		#predation on this organism
		preds = np.zeros((organisms[i].consumed.shape[0], grid, grid, 2))
		predProps = np.zeros((organisms[i].consumed.shape[0], 4))
		
		for j in range(organisms[i].consumed.shape[0]):
			index =  organisms[i].consumed[j]
			preds[j] = reformatPandE(energies[index], pollutions[index])		
			predProps[j] = np.array([organisms[index].predation,organisms[index].maxdist, efficiency, pTransfer]) 
		
		#print(organisms[i].consumed.shape[0])
		if(organisms[i].consumed.shape[0] !=0):
			eatenRemE, eatenRemP, consumeAddE, consumeAddP = consume.consume(reformatPandE(energies[i], pollutions[i]), preds, predProps, grid, dt)
			#graphics.drawEnergy(consumeAddP[0], np.zeros((grid, grid)), np.zeros((grid, grid)))
		else:
			eatenRemE = np.zeros((grid, grid))
			eatenRemP = np.zeros((grid, grid))
			consumeAddE = np.zeros((grid, grid))
			consumeAddP = np.zeros((grid, grid))
			
		
		
		#giving predators energy and pollution
		for j in range(organisms[i].consumed.shape[0]):
			index =  organisms[i].consumed[j]
			
			change[index][0]+=consumeAddE[j]*dt
			change[index][1]+= consumeAddP[j]*dt
		
		change[i][0] += eatenRemE*dt
		change[i][1] += eatenRemP*dt	
		
		#graphics.drawEnergy(np.zeros(change[2][0].shape), -change[2][0], np.zeros(change[i][0].shape))
		for j in range(energies.shape[0]):
			energies[j] += change[j][0]
			pollutions[j] += change[j][1]

		change = np.zeros((organisms.shape[0], 2, grid, grid))
		
		#TODO: Figure out pollution with below 2 functions
		diffus = diffusion(organisms[i].diffusion, energies[i], dt)
		diffusP = diffusion(organisms[i].diffusion, pollutions[i], dt)
		met = metabolism(energies[i], organisms[i], dt)
		#metP = metabolism(pollutions, organisms[i], dt)
		polluteAbsorb = pollute.envirPoll(ambient_pollution, energies[i], pollutions[i], absorbtionRate, dt)
		
		#graphics.drawEnergy(consumeAddE[0], np.zeros(consumeAddE[0].shape), np.zeros(consumeAddE[0].shape))

		#graphics.drawEnergy(np.zeros(eatenRemE.shape), -eatenRemE, np.zeros(eatenRemE.shape))

		#TODO
		pollutions[i]+=diffusP*dt +polluteAbsorb#+met
		energies[i]+= diffus*dt+met

		kill, remP = pollutant.pollutApply(energies[i], pollutions[i], organisms[i].ld50, dt)
		
		energies[i]+=kill
		pollutions[i]+=remP
		if(organisms[i].ambient):
			producers.append(i)

		
	#handle multiple producers
	
	change = np.zeros((organisms.shape[0], 2, grid, grid))
	prods = np.zeros((len(producers), grid, grid, 2))
	prodProps = np.zeros((len(producers), 4))

	for j in range(len(producers)):
		index = producers[j]
		prods[j] = reformatPandE(energies[index], pollutions[index])
		prodProps[j] = np.array([organisms[index].predation,organisms[index].maxdist, efficiency, 0])
		
	x, y, producerAdd, z =  consume.consume(epambient, prods, prodProps, grid, dt)

	for j in range(len(producers)):
		index = producers[j]
		#TODO
		change[index][0] += producerAdd[j]*dt
	#graphics.drawDebug(np.array([change[0][0], change[1][0], change[2][0]], np.array(["plant", "fish", "osprey"])))
 	#add energies and pollutions
	for i in range(energies.shape[0]):
		energies[i] += change[i][0]
		pollutions[i] += change[i][1]
	
	return energies, pollutions



	


	

