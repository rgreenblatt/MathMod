import initial
import numpy as np
import classes
import generateScenario as gen
import sys
import graphics
energyByTimeP = []
energyByTimeH = []
energyByTimeC = []
gen = gen.setup()

grid = 100

plant=classes.Organism(0)
fish=classes.Organism(1)
osprey=classes.Organism(2)

pplant=np.full((grid,grid),0.0)
pfish=np.full((grid,grid),0.0)
posprey=np.full((grid,grid),0.0)

energies = np.array([gen[0], gen[1],gen[2]])
pollutions = np.array([pplant, pfish, posprey])
graphics.drawEnergy(energies[0], energies[1], energies[2])
for i in range(10):
	energyByTimeP.append(energies[0])
	energyByTimeH.append(energies[1])
	energyByTimeC.append(energies[2])
	energies, pollutions = initial.iter_model(np.array([plant, fish, osprey]), energies, pollutions, .2, 1, grid, .8, .6)
	#graphics.drawEnergy(energies[0], energies[1], energies[2])
	print(energies)
	sys.stdout.flush()
#print(energyByTimeH[0])
sys.stdout.flush()
graphics.animEnergy(np.array(energyByTimeP), np.array(energyByTimeH), np.array(energyByTimeC))
