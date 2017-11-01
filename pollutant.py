import math
import graphics
import numpy as np

def logistic(center,conc,rate=2):
    return 1/(1+math.e**(-rate*(conc-center)))


def pollutApply(energy,pollution,ld50, dt):
    out=np.zeros(energy.shape)
    outP =np.zeros(energy.shape) 
    for i in range(energy.shape[0]):
        for k in range(energy.shape[1]):
            change=logistic(ld50,pollution[i][k]/energy[i][k],rate=(5)*ld50)
            out[i][k]=-dt*change*energy[i][k]/10
            outP[i][k]=-dt*change*pollution[i][k]/10
    return out, outP

