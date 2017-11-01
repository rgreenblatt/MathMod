import initial
import numpy as np
import classes
import generateScenario as gen
import sys
import graphics
import biomass


grid = 100
dt = .15
tFin = 30
plant_ambient = .6
efficiency = .4
pTransfer = 1
absorbtionRate = 2


energyByTimeP = np.zeros((tFin, grid, grid))
energyByTimeH =  np.zeros((tFin, grid, grid)) 
energyByTimeC =  np.zeros((tFin, grid, grid))

plant=classes.Organism(0, .9, .5, .2, 2, "plant", np.array([1]), True, .2)
fish=classes.Organism(1, .2, .7, .6, 10, "fish", np.array([2]), False, .2)
osprey=classes.Organism(2, .1, .7, .8, 20, "osprey", np.array([]), False, .2)

organisms = np.array([plant, fish, osprey])

generate = gen.setup(np.array([150, 50, 24]))


pEnviron =gen.start(5)   

pplant=np.full((grid,grid),0.0)
pfish=np.full((grid,grid),0.0)
posprey=np.full((grid,grid),0.0)

energies = np.array([generate[0], generate[1],generate[2]])
pollutions = np.array([pplant, pfish, posprey])
#graphics.drawEnergy(energies[0], energies[1], energies[2])
for i in range(tFin):

	energies, pollutions = initial.iter_model(organisms, energies, pollutions, dt, grid, efficiency, pTransfer, .5, pEnviron, absorbtionRate)
	
	
	energyByTimeP[i]= energies[0]
	energyByTimeH[i] = energies[1]
	energyByTimeC[i] = energies[2]
	#graphics.drawEnergy(energies[0], energies[1], energies[2])
	#print(energies)
	#graphics.drawEnergy(energies[0], energies[1], energies[2])
	#print(np.sum(energies[0]))
	#print(np.sum(energies[1]))
	#print(np.sum(energies[2]))
	#print("")
	sys.stdout.write("\r"+str(i)+"\033[K")
	sys.stdout.flush()

sys.stdout.flush()

energiesByTime = np.swapaxes(np.array([energyByTimeP, energyByTimeH, energyByTimeC]), 0, 1)

biomass.bioGraph(energiesByTime, "run initial")
graphics.animEnergy(np.array(energyByTimeP), np.array(energyByTimeH), np.array(energyByTimeC))

