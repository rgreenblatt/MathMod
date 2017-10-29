import numpy as np
import circleGener as circ
import math
import classes
import sys
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
				print(pred)
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
	

					
