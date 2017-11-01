import numpy as np
import matplotlib.pyplot as plt
def bioGraph(array, name):
    out = np.sum(array,axis=(2,3))
    times=np.arange(out.shape[0])
    plt.plot(times,out[:,0],'r--',times,out[:,1],'bs',times,out[:,2],'g^')
    plt.show()
    plt.savefig(name)
    plt.clf
#hi=np.zeros((100,100,100,100))
#print(bioGraph(hi))
