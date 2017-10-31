import initial
import numpy as np
import classes
import generateScenario as gen
import sys
import graphics
energyByTimeP = []
energyByTimeH = []
energyByTimeC = []


grid = 100
dt = 1
tFin = 10
plant_ambient = .2
efficiency = .8
pTransfer = .6


plant=classes.Organism(0, .9, .05, .2, 2, "plant", np.array([0]), True)
fish=classes.Organism(1, .6, .2, .4, 4, "fish", np.array([1]), False)
osprey=classes.Organism(2, .6, .4, .6, 6, "osprey", np.array([]), False)

organisms = np.array([plant, fish, osprey])

generate = gen.setup(organisms)

pplant=np.full((grid,grid),0.0)
pfish=np.full((grid,grid),0.0)
posprey=np.full((grid,grid),0.0)

energies = np.array([generate[0], generate[1],generate[2]])
pollutions = np.array([pplant, pfish, posprey])
graphics.drawEnergy(energies[0], energies[1], energies[2])
for i in range(tFin):
	energyByTimeP.append(energies[0])
	energyByTimeH.append(energies[1])
	energyByTimeC.append(energies[2])
	energies, pollutions = initial.iter_model(organisms, energies, pollutions, dt, grid, efficiency, pTransfer, .5)
	#graphics.drawEnergy(energies[0], energies[1], energies[2])
	print(energies)
	sys.stdout.flush()
#print(energyByTimeH[0])
sys.stdout.flush()
graphics.animEnergy(np.array(energyByTimeP), np.array(energyByTimeH), np.array(energyByTimeC))
