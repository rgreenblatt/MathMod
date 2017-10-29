import numpy as np
import circleGener as circ
import math
def consume(eprey, epred, porganisms, grid):
	for i in range(grid):
		for k in range(grid):
			preds = []
			for h in range(len(epred)):
				pred = circ.collect(i, k, porganisms[h].maxdist)
				for i in range(len(pred)):
					if pred[i][0]>=0 or pred[i][1]>=0 or epred[pred[i][0]][pred[i][1] ==0 or pred[i][0] > grid or pred[i][1] > grid:
						del pred[i]
				preds.append(pred)
			nArray = []
			for h in range(len(preds)):
				for p in pred[h]:
					#N = Epred*predation constant*(1-dist/maxdis)
					nArray.append(epred[p[0]][p[1]]*porganisms[h].predation*(1-math.sqrt(math.pow(i-p[0], 2)+ math.pow(k-p[1], 2))/porganisms[h].maxdist))
			if sum(nArray) > eprey[i][k]:
				eprey[i][k] = 0
				factor = eprey[i][k]/sum(nArray)
				for h in range(len(preds)):
					for p in pred[h]:
						epred[p[0]][p[1]]+=nArray[i]*factor
						i+=1
			else:
				eprey[i][k] -= sum(nArray)		
				for h in range(len(preds)):
					for p in pred[h]:
						epred[p[0]][p[1]]+=nArray[i]
						i+=1


					
