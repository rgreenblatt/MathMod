import numpy as np

grid = 100
eposprey=np.tile(np.array([[1.0, 0.0]]), (grid,grid,1))
print(eposprey)
eposprey = np.swapaxes(eposprey, 2, 0)
print(np.swapaxes(eposprey, 0, 2))
