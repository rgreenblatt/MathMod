import initial
import numpy as np
import classes
import generateScenario as gen
import sys
import graphics



grid = 100
dt = .5
tFin = 100
plant_ambient = .6
efficiency = .8
pTransfer = .6
absorbtionRate = .1


energyByTimeP = np.zeros((tFin, 100, 100))
energyByTimeH =  np.zeros((tFin, 100, 100)) 
energyByTimeC =  np.zeros((tFin, 100, 100))

plant=classes.Organism(0, .9, .9, .5, 2, "plant", np.array([1]), True)
fish=classes.Organism(1, .2, .7, .1, 20, "fish", np.array([2]), False)
osprey=classes.Organism(2, .1, .7, .2, 10, "osprey", np.array([]), False)

organisms = np.array([plant, fish, osprey])

generate = gen.setup(np.array([10, 1, .1]))


pEnviron = gen.start(1)

pplant=np.full((grid,grid),0.0)
pfish=np.full((grid,grid),0.0)
posprey=np.full((grid,grid),0.0)

energies = np.array([generate[0], generate[1],generate[2]])
pollutions = np.array([pplant, pfish, posprey])
graphics.drawEnergy(energies[0], energies[1], energies[2])
for i in range(tFin):

	energies, pollutions = initial.iter_model(organisms, energies, pollutions, dt, grid, efficiency, pTransfer, .5, pEnviron, absorbtionRate)
	print(i)
	
	energyByTimeP[i]= energies[0]
	energyByTimeH[i] = energies[1]
	energyByTimeC[i] = energies[2]
	#graphics.drawEnergy(energies[0], energies[1], energies[2])
	#print(energies)
	#graphics.drawEnergy(energies[0], energies[1], energies[2])
	sys.stdout.flush()
print(energyByTimeH[0])

print(energyByTimeH[13])

print(np.array(energyByTimeH).shape)
sys.stdout.flush()
graphics.animEnergy(np.array(energyByTimeP), np.array(energyByTimeH), np.array(energyByTimeC))
