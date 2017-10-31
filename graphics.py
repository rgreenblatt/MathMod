import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
def drawEnergy(producer, herbivore, carnivore,name=None):
    colors = np.array([producer, herbivore, carnivore])
    colors = np.log(colors+1.)
    colors = np.swapaxes(colors, 0, 2)
    colors = np.maximum(colors/(np.amax(colors, axis = (0,1))+0.001),0)
    #plt.pcolor(producer, herbivore, carnivore)
    #plt.show()
    plt.imshow(colors)
    fig = plt.gcf()
    if name != None:
        fig.canvas.set_window_title(name)
    else:
        fig.canvas.set_window_title('Energy Figure')
    plt.show()

def drawDebug(data,name=None):
	f, axarr = plt.subplots(data.shape[0])
	for i in range(data.shape[0]):
		colors = np.log(data[i] + 1.)
		colors = np.swapaxes(colors, 0, 2)
		colors = np.maximum(colors/(np.amax(colors, axis = (0,1))+0.001),0)
		axarr[i].imshow(colors)
		if name!=None:
			axarr[i].set_title(name[i])
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
