import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
def drawEnergy(producer, herbivore, carnivore):
    colors = np.array([producer, herbivore, carnivore])
    colors = np.log(colors+1.)
    colors = np.swapaxes(colors, 0, 2)
    colors = np.maximum(colors/(np.amax(colors, axis = (0,1))+0.001),0)
    #plt.pcolor(producer, herbivore, carnivore)
    #plt.show()
    plt.imshow(colors)
    plt.show()

def animEnergy(producer, herbivore, carnivore,maximums=None):
    
    colors = np.array([producer, herbivore, carnivore])
    colors = np.log(colors+1.)
    colors = np.swapaxes(colors, 0, 3)
    colors = np.swapaxes(colors, 1, 2)
    if maximums == None:
        maximums = np.amax(colors, axis = (0,1))
        minimums = np.amin(colors, axis = (0,1))
        colors = np.maximum((colors-minimums)/(maximums-minimums+0.001),0)
    else:
    	colors = np.maximum(colors/maximums,0)
    colors = np.swapaxes(colors,0,2)
    #plt.pcolor(producer, herbivore, carnivore)
    #plt.show()
    for i in range(colors.shape[0]):
        plt.imshow(colors[i])
        #print(str(i)+"\r")
        name="img%.2d"%(i)
        plt.savefig(name)
        plt.clf()
