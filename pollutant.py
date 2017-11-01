import math
import graphics
import numpy as np

def logistic(center,conc,rate=2):
    return 1/(1+math.e**(-rate*(conc-center)))


def pollutApply(energy,pollution,ld50):
    out=np.zeros(energy.shape)
    for i in range(energy.shape[0]):
        for k in range(energy.shape[1]):
            change=logistic(ld50,pollution[i][k],rate=5*ld50)
            if i==1 and k==1:
                print(change)
            out[i][k]=-change*energy[i][k]
    return out

