import initial
import numpy as np
import classes
import generateScenario as gen
import sys
import graphics
import biomass


grid = 100
dt = .15
tFin = 35
plant_ambient = .6
efficiency = .4
pTransfer = 40
absorbtionRate = 10



plant=classes.Organism(0, .9, .5, .2, 2, "plant", np.array([1]), True, .1)
fish=classes.Organism(1, .2, .7, .6, 10, "fish", np.array([2]), False, .1)
osprey=classes.Organism(2, .1, .7, .8, 60, "osprey", np.array([]), False, .1)

organisms = np.array([plant, fish, osprey])





energyByTimeP = np.zeros((tFin, grid, grid))
energyByTimeH =  np.zeros((tFin, grid, grid))
energyByTimeC =  np.zeros((tFin, grid, grid))


energyP = np.full((grid, grid), 0.17085959)

energyH = np.full((grid, grid), 0.03449875)

energyC = np.full((grid, grid),  0.01910742)

energies  = np.array([energyP, energyH, energyC])

pEnviron = gen.start(10)
graphics.drawEnergy(pEnviron, np.zeros((grid, grid)), np.zeros((grid, grid)))

pplant=np.full((grid,grid),0.0)
pfish=np.full((grid,grid),0.0)
posprey=np.full((grid,grid),0.0)

pollutions = np.array([pplant, pfish, posprey])
#graphics.drawEnergy(energies[0], energies[1], energies[2])
print("nextRun")
for i in range(tFin):
	#graphics.drawEnergy(pollutions[0], pollutions[1], pollutions[2])
	energies, pollutions = initial.iter_model(organisms, energies, pollutions, dt, grid, efficiency, pTransfer, .5, pEnviron, absorbtionRate)
	sys.stdout.write("\r"+str(i)+"\033[K")
	sys.stdout.flush()
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
	sys.stdout.flush()

sys.stdout.flush()

energiesByTime = np.swapaxes(np.array([np.zeros((tFin, grid, grid)), energyByTimeH, energyByTimeC]), 0, 1)

biomass.bioGraph(energiesByTime, "pollution")
graphics.animEnergy(np.array(energyByTimeP), np.array(energyByTimeH), np.array(energyByTimeC))
