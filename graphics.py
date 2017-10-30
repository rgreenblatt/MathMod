import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def drawEnergy(population):
    plt.pcolor(population)
    plt.show()


def animEnergy(total):
    for i in range(0,total.shape[0],10):
        plt.pcolor(total[i])
        print(str(i)+"\r")
        name="img%.2d"%(i//10)
        plt.savefig(name)
        plt.clf()
