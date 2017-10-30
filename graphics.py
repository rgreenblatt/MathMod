import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
def drawEnergy(producer, herbivore, carnivore):
    colors = np.array([producer, herbivore, carnivore])
    colors = np.log(colors+1.)
    colors = np.swapaxes(colors, 0, 2)
    colors = np.maximum(colors/np.amax(colors, axis = (0,1)),0)
    #plt.pcolor(producer, herbivore, carnivore)
    #plt.show()
    plt.imshow(colors)
    plt.show()

def animEnergy(producer, herbivore, carnivore):
    
    colors = np.array([producer, herbivore, carnivore])
    colors = np.swapaxes(colors, 0, 3)
    colors = np.swapaxes(colors, 0, 1)
    colors = colors/np.amax(colors, axis = (0,1,2))
    #plt.pcolor(producer, herbivore, carnivore)
    #plt.show()
    plt.imshow(colors)
    plt.show()
    for i in range(colors.shape[0]):
        plt.imshow(colors[i])
        print(str(i)+"\r")
        name="img%.2d"%(i)
        plt.savefig(name)
        plt.clf()
