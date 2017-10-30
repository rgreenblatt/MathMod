import numpy as np
import circleGener as circ
import math
import classes
import sys
from scipy import signal
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
def consume(ePreyOrig,ePredOrig,pOrganisms,grid,dt):
	predator_contribution = np.copy(ePredOrig)
	for i in range(ePredOrig.shape[0]):
		predator_contribution[i]=convolveSingle(ePredOrig[i],pOrganisms[i,1],grid)
	predator_contribution = predator_contribution * pOrganisms[:,0]*dt
	predator_sum = np.sum(predator_contribution,axis=0)
	norm_constants = np.where(predator_sum<ePreyOrig,1,ePreyOrig/predator_sum)	
	
	eaten = np.zeros((ePredOrig.shape))
	for i in range(eaten.shape[0]):
		eaten[i]=convolveSingle(norm_constants,pOrganisms[i,1],grid)
	#norm_constants[1:]=norm_constants[1:]*norm_constants[0]
	eaten = eaten * ePredOrig * pOrganisms[:,0]*dt
	prey_survived = ePreyOrig - predator_sum*norm_constants
	print(prey_survived)
	eaten = eaten*pOrganisms[:,2]
	final_predator_energies = ePredOrig + eaten
	print(final_predator_energies)
	return prey_survived, final_predator_energies


def convolveSingle(organism,radius,grid):
	circle = circ.gener(radius)
	convolution = signal.convolve2d(organism,circle,boundary='wrap',mode='same')
	return convolution

					
