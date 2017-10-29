
            if k==grid-1 and i==grid-1:
                neighbors=[energies[i-1][k],energies[i-1][k-1],energies[i][k-1]]
            elif k==grid-1:
                neighbors=[energies[i-1][k],energies[i+1][k],energies[i][k-1],energies[i+1][k-1],energies[i-1][k-1]]
            elif i==grid-1:
                neighbors=[energies[i-1][k],energies[i-1][k+1],energies[i][k-1],energies[i][k+1],energies[i-1][k-1]]
            elif k==0 and i==0:
                neighbors=[energies[i+1][k],energies[i][k+1],energies[i+1][k+1]]
            elif k==0:
                neighbors=[energies[i][k+1],energies[i-1][k],energies[i+1][k],energies[i-1][k+1],energies[i+1][k+1]]
            elif i==0:
                neighbors=[energies[i][k+1],energies[i+1][k],energies[i][k-1],energies[i+1][k+1],energies[i+1][k-1]]
            else:
                neighbors=[energies[i-1][k],energies[i+1][k],energies[i][k+1],energies[i][k-1],energies[i+1][k+1],energies[i-1][k+1],energies[i+1][k-1],energies[i-1][k-1]]
