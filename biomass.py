import numpy as np
import matplotlib.pyplot as plt
def bioGraph(array):
    colors=('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')
    out=np.zeros((array.shape[1],array.shape[0]))
    for i in range(out.shape[0]):
        for k in range(out.shape[1]):
            biomass=np.sum(array[i][k])
            out[k][i]=biomass
    times=np.arange(out.shape[0])
    [plt.plot(times,out[k]),colors[k] for k in range(out.shape[0])]
    plt.show()

hi=np.zeros((100,100,100,100))
print(bioGraph(hi))
