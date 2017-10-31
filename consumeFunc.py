import numpy as np
import circleGener as circ
import math
import classes
import sys
from scipy import signal
import graphics
'''
def consume(epreyOrig, epredOrig, porganisms, grid, dt):
	eprey = np.copy(epreyOrig)
	epred = np.copy(epredOrig)
	for i in range(grid):
		print(i)
		sys.stdout.flush()
		for k in range(grid):
			preds = []
			for h in range(len(epred)):
				pred = circ.collect(i, k, porganisms[h][1])
				#print(pred)
				e = 0
				while e < len(pred):
					if pred[e][0] < 0 or pred[e][1] < 0 or pred[e][0] > grid-1 or pred[e][1] > grid-1:
						del pred[e]
					elif epredOrig[h][pred[e][0]][pred[e][1]] == 0:
						del pred[e]
					else:
						e+=1
				preds.append(pred)
			nArray = []
			for h in range(len(preds)):
				for p in preds[h]:
					#N = Epred*predation constant*(1-dist/maxdis)
					#print(p)
					nArray.append(dt*epred[h][p[0]][p[1]]*porganisms[h][0]*(1-math.sqrt(math.pow(i-p[0], 2)+ math.pow(k-p[1], 2))/porganisms[h][1]))
			if sum(nArray) > eprey[i][k]:
				epreyOrig[i][k] = 0
				factor = eprey[i][k]/sum(nArray)
				r = 0
				for h in range(len(preds)):
					for p in preds[h]:
#						print(porganisms[h][2])
#						print(nArray[r])
#						print(p[0])
#						sys.stdout.flush()
#						print(epred[h][p[0]][p[1]])
						epredOrig[h][p[0]][p[1]]+=porganisms[h][2]*nArray[r]*factor
						r+=1
			else:
				r = 0
				epreyOrig[i][k] -= sum(nArray)		
				for h in range(len(preds)):
					for p in preds[h]:
						epredOrig[h][p[0]][p[1]]+=porganisms[h][2]*nArray[r]
						r+=1

'''

def consume(ePreyOrig,ePredOrig, pOrganisms,grid,dt):
	
	graphics.drawEnergy(ePreyOrig[:,:,0], ePredOrig[0,:,:,0], np.zeros(ePreyOrig[:,:,0].shape))
	predator_contribution = np.copy(ePredOrig)
	
	#calculates max amount eaten based on predator counts
	for i in range(ePredOrig.shape[0]):
		predator_contribution[i]=convolveSingle(ePredOrig[i],pOrganisms[i,1],grid)
	predator_contribution = predator_contribution * pOrganisms[:,0]*dt
	predator_sum = np.sum(predator_contribution,axis=0)
	
	#limits the amount eaten to the amount available
	norm_constants = np.where(np.logical_and(predator_sum>ePreyOrig, predator_sum != 0),ePreyOrig/predator_sum,1)

	eaten = np.zeros((ePredOrig.shape))
	for i in range(eaten.shape[0]):
		eaten[i]=convolveSingle(norm_constants,pOrganisms[i,1],grid)
	#print(norm_constants)
	norm_constants[1:]=np.minimum(norm_constants[1:],norm_constants[0])

	eaten = eaten * ePredOrig*dt*pOrganisms[:,0]
	eaten = np.swapaxes(eaten, 1, 3)
	eat = eaten[:,0]
	pollute = eaten[:,1]
	prey_reduction = -predator_sum*norm_constants
	prey_reduction = np.swapaxes(prey_reduction, 0, 2)
#	prey_survived = ePreyOrig - prey_reduction
#	print(prey_survived)
	pollute = pollute*pOrganisms[:,3]
	#print(eat)
	eaten = eat*pOrganisms[:,2]
	graphics.drawEnergy(norm_constants[:,:,0], predator_sum[:,:,0], np.zeros(ePreyOrig[:,:,0].shape))
#	final_predator_energies = ePredOrig + eaten
#	print(final_predator_energies)
#	return prey_survived, final_predator_energies
	#print(eaten)
	return prey_reduction[0], prey_reduction[1], eaten, pollute


'''
#this is old version
def consume(epPreyOrig,epPredOrig, pOrganisms,grid,dt):
	
	predator_contribution = np.copy(ePredOrig)
	
	#calculates max amount eaten based on predator counts
	for i in range(ePredOrig.shape[0]):
		predator_contribution[i]=convolveSingle(ePredOrig[i],pOrganisms[i,1],grid)
	predator_contribution = predator_contribution * pOrganisms[:,0]*dt
	predator_sum = np.sum(predator_contribution,axis=0)

	#limits the amount eaten to the amount available
	norm_constants = np.where(predator_sum<ePreyOrig,1,ePreyOrig/predator_sum)	
	eaten = np.zeros((ePredOrig.shape))
	for i in range(eaten.shape[0]):
		eaten[i]=convolveSingle(norm_constants,pOrganisms[i,1],grid)
	norm_constants[1:]=np.min(norm_constants[1:],norm_constants[0])

	eaten = eaten * ePredOrig * pOrganisms[:,0]*dt
	prey_reduction = -predator_sum*norm_constants
#	prey_survived = ePreyOrig - prey_reduction
#	print(prey_survived)
	eaten = eaten*pOrganisms[:,2]
#	final_predator_energies = ePredOrig + eaten
#	print(final_predator_energies)
#	return prey_survived, final_predator_energies
	return prey_reduction, eaten
'''
def convolveSingle(prop,radius,grid):
	circle = circ.gener(radius)
	convolution = np.zeros(prop.shape)
	for i in range(prop.shape[0]):
		convolution[i] = signal.convolve2d(prop[i],circle,boundary='wrap',mode='same')
	return convolution

					
